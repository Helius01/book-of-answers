#!/usr/bin/env python3
"""Lint Twee 3 sources: broken links, dead ends, unset variables, flag typos, text length.

Usage: python3 scripts/lint.py src [more dirs or files...]
Exit code 1 if any error is found. Warnings never fail the build.
"""
import re
import sys
from pathlib import Path

SPECIAL = {
    "StoryTitle", "StoryData", "StoryInit", "StoryCaption", "StoryMenu", "StoryBanner",
    "StorySubtitle", "StoryAuthor", "StoryInterface", "StoryShare", "PassageReady",
    "PassageDone", "PassageHeader", "PassageFooter",
}
# Passages with these tags may have no outgoing link and are not word-count checked.
NO_EXIT_TAGS = {"end", "widget", "script", "stylesheet", "answer", "debug", "ui", "clue"}
CODE_TAGS = {"widget", "script", "stylesheet"}

HEADER = re.compile(r"^::\s*(.*?)\s*(?:\[(.*?)\])?\s*(?:\{.*\})?\s*$")
WIKI_LINK = re.compile(r"\[\[(.*?)\]\]")
MACRO_LINK = re.compile(r"<<(?:link|button)\s+([\"'])(?:.*?)\1\s+([\"'])(.*?)\2")
MACRO_GOTO = re.compile(r"<<(?:goto|include)\s+([\"'])(.*?)\1")
# <<check guess "answer" "okPassage" "failPassage">> and <<mirror ...>> (same args)
MACRO_CHECK = re.compile(r"<<(?:check|mirror)\s+(.*?)>>")
# <<hurry "tooSlowPassage">>
MACRO_HURRY = re.compile(r"<<hurry\s+([\"'])(.*?)\1")
DYNAMIC_LINK = re.compile(r"<<(?:link|button|goto)\s[^>]*`")
COMMENT = re.compile(r"/\*.*?\*/", re.S)
QUOTED = re.compile(r"([\"'])(.*?)\1")
VAR = re.compile(r"\$([A-Za-z_]\w*)")
FLAG_READ = re.compile(r"\$flags\.(\w+)")
FLAG_SET = re.compile(r"\$flags\.(\w+)\s+to\b")


def parse(sources):
    """sources: {filename: text} -> list of (name, tags, body, filename)."""
    passages = []
    for fname, text in sources.items():
        cur = None
        for line in text.splitlines():
            if line.startswith("::"):
                m = HEADER.match(line)
                cur = [m.group(1), set((m.group(2) or "").split()), [], fname]
                passages.append(cur)
            elif cur is not None:
                cur[2].append(line)
    return [(n, t, "\n".join(b), f) for n, t, b, f in passages]


def wiki_target(inner):
    inner = inner.split("][", 1)[0]  # drop setter component
    if "|" in inner:
        return inner.rsplit("|", 1)[1]
    if "->" in inner:
        return inner.rsplit("->", 1)[1]
    if "<-" in inner:
        return inner.split("<-", 1)[0]
    return inner


def targets(body):
    """Return (literal targets, has_dynamic_exit)."""
    body = COMMENT.sub(" ", body)
    out = [wiki_target(m.group(1)).strip() for m in WIKI_LINK.finditer(body)]
    out += [m.group(3) for m in MACRO_LINK.finditer(body)]
    out += [m.group(2) for m in MACRO_GOTO.finditer(body)]
    out += [m.group(2) for m in MACRO_HURRY.finditer(body)]
    for m in MACRO_CHECK.finditer(body):
        out += [q.group(2) for q in QUOTED.finditer(m.group(1))][1:]
    dynamic = [t for t in out if "$" in t or "_" == t[:1] or "`" in t]
    literal = [t for t in out if t not in dynamic]
    return literal, bool(dynamic) or bool(DYNAMIC_LINK.search(body))


def plain_text(body):
    body = COMMENT.sub(" ", body)
    body = re.sub(r"<<.*?>>", " ", body, flags=re.S)
    body = WIKI_LINK.sub(lambda m: m.group(1).split("][")[0].split("|")[0].split("->")[0], body)
    body = re.sub(r"<[^>]+>", " ", body)
    body = re.sub(r"@@[\w.\-;]*;|@@", " ", body)
    return body


def lint(sources):
    passages = parse(sources)
    errors, warnings = [], []
    names = {}
    for name, _, _, fname in passages:
        if name in names:
            errors.append(f"duplicate passage '{name}' in {names[name]} and {fname}")
        names[name] = fname

    init = next((b for n, _, b, _ in passages if n == "StoryInit"), "")
    init_vars = set(VAR.findall(init))
    all_text = "\n".join(b for _, t, b, _ in passages if "script" not in t)
    flags_set = set(FLAG_SET.findall(all_text))

    for name, tags, body, fname in passages:
        where = f"{fname}: '{name}'"
        if "stylesheet" in tags or name == "StoryData":
            continue
        literal, dynamic = targets(body)
        for t in literal:
            if t not in names:
                errors.append(f"{where}: broken link to '{t}'")
        if not literal and not dynamic and name not in SPECIAL and not tags & NO_EXIT_TAGS:
            errors.append(f"{where}: dead end (no outgoing link; tag [end] if intended)")
        if "script" not in tags:
            for v in sorted(set(VAR.findall(body)) - init_vars):
                errors.append(f"{where}: ${v} is never set in StoryInit")
            for f in sorted(set(FLAG_READ.findall(body)) - flags_set):
                warnings.append(f"{where}: $flags.{f} is read but never set (typo?)")
        if name in SPECIAL or tags & (NO_EXIT_TAGS | CODE_TAGS):
            continue
        text = plain_text(body)
        words = len(text.split())
        if words > 120:
            warnings.append(f"{where}: {words} words (max 120)")
        for sentence in re.split(r"[.?!\n]+", text):
            n = len(sentence.split())
            if n > 12:
                warnings.append(f"{where}: {n}-word sentence: '{' '.join(sentence.split())[:60]}...'")
    return errors, warnings


def main(paths):
    files = []
    for p in map(Path, paths):
        files += sorted(p.rglob("*.twee")) if p.is_dir() else [p]
    errors, warnings = lint({str(f): f.read_text(encoding="utf-8") for f in files})
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("ERROR:", e)
    print(f"{len(errors)} error(s), {len(warnings)} warning(s) in {len(files)} file(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or ["src"]))
