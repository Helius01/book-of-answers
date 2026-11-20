# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

"The Book of Answers": a choice-based text adventure for intermediate English learners. It is written in Twee 3 for the SugarCube 2.37.3 story format, compiled with Tweego into a single HTML file, and published on itch.io. The story, characters and development plan live in a Claude Docs doc ("The Book of Answers — Text Adventure Storyline", with a "Development plan" tab), not in this repo.

## Commands

```sh
make build   # lint, then release build -> dist/index.html (no debug panel)
make dev     # SugarCube test mode + debug/ -> dist/dev.html
make watch   # same as dev, rebuilds on save
make lint    # python3 scripts/lint.py src debug  (exit 1 on errors)
make test    # python3 scripts/test_lint.py  (self-check for the linter)
```

Tweego 2.1.1 is installed at `~/.local/bin/tweego`. SugarCube is vendored in `.storyformats/sugarcube-2/`, and Tweego finds it there automatically. `format-version` in `StoryData` must match that copy.

Tweego does **not** detect broken links. `scripts/lint.py` does: broken links, dead ends, variables not set in `StoryInit`, duplicate passage names, `$flags.x` read but never set, and writing-rule warnings (passage > 120 words, sentence > 12 words). When you add a macro that takes a passage name as an argument, teach `targets()` in `lint.py` about it.

## Architecture

- `src/systems.twee`: `StoryData` (IFID and title are frozen, because the save key comes from them), `StoryInit` (all 9 state variables), `StoryScript`, widgets, and the `darkness` passage.
- `src/ui.twee`: side bar (`StoryCaption`: candle bar and satchel), `StoryMenu` Journal dialog, and `BS_*` "Book Speaks" answer passages tagged `[answer]`.
- `src/actN.twee`: one file per act. Passage names are prefixed `A<act>_`. Each act runs `A#_start` (sets `$act`) → missions → puzzle → big choice → `A#_end [autosave]`. Branches merge again at `A#_end`; choices survive as variables, not as separate storylines.
- `debug/debug.twee`: `DebugPanel`, compiled only into dev builds. `StoryCaption` includes it only if `Story.has("DebugPanel")`.

Game rules worth knowing before editing passages:
- Change state only through the widgets: `<<spend n>>` (wax; does nothing until `$flags.candle_lit`), `<<heart n>>`, `<<trust "who" n>>`, `<<give>>`/`<<take>>` (6-item satchel), `<<speak "id">>`.
- Typed puzzles: `<<textbox "_guess" "">>` plus a `<<link>>` that calls `<<check _guess "ans|alt" "okPassage" "failPassage">>` or `<<mirror ...>>` (`<<mirror>>` also counts `$mirrorSolved` once per puzzle). The **fail passage** spends the 3 wax.
- `Config.history.maxStates = 1`: there is no undo by design.
- `Config.navigation.override` sends every move to `darkness` when wax is 0, unless the target is tagged `[dark]`.
- Autosave uses the 2.37 API (`Save.browser.auto.save()` on `:passagedisplay`). `Config.saves.autosave` is deprecated in 2.37.
- `@class` on an element replaces its static `class`; put every class name in the expression.

Writing rules for player-facing text: sentences under 12 words, common words, second person ("you"), 2–3 choices per passage, end each scene on a hook.

## Status

Phases 0–2 are done: all 7 acts, plus the 5 endings (`END_*`, tagged `[end dark]`) in `act7.twee`. The Phase 1 playtest was skipped on purpose, so nobody has played it yet. The wax budget is a first guess: an honest, careful run ends with about 50 wax, and a lying, careless run with about 5 (the doc targets about 15 for careful play). Tune it after playtests. Ending gates are in `A7_choice`:
- Heart < 3: Ashes.
- Heart ≥ 8 and the captive saved: Truth.
- Heart ≥ 6: Gift.
- Keep is always available.
- Secret needs `$mirrorSolved` ≥ 4 (puzzles in A1, A4, A5, A6) and all three trust scores ≥ 7.

Phase 3 polish (heartbeat lines, timers, parchment CSS, sound) is not started.
