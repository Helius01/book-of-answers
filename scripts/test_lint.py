#!/usr/bin/env python3
"""Self-check for lint.py: each rule must fire on a known-bad story and stay quiet on a good one."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lint import lint  # noqa: E402

BAD = """
:: StoryInit
<<set $wax to 100>>

:: Start
<<if $flags.typo>>x<</if>>[[Go|Nowhere]] [[Fine|Stuck]]

:: Stuck
You stand still. $gold coins.

:: Puzzle
<<textbox "_g" "">><<link "Try">><<check _g "a" "Start" "Missing">><</link>>

:: Chase
<<hurry "Gone">>

:: Start
Duplicate.
"""

GOOD = """
:: StoryInit
<<set $wax to 100; $flags to {}>>

:: Start
<<set $flags.seen to true>><<if $flags.seen>>Hi.<</if>> [[Next->Done]] <<link "Back" `"St" + "art"`>><</link>>

:: Done [end]
The end.
"""

errors, warnings = lint({"bad.twee": BAD})
text = "\n".join(errors)
assert "broken link to 'Nowhere'" in text, errors
assert "broken link to 'Missing'" in text, errors
assert "broken link to 'Gone'" in text, errors
assert "'Stuck': dead end" in text, errors
assert "$gold is never set" in text, errors
assert "duplicate passage 'Start'" in text, errors
assert any("$flags.typo" in w for w in warnings), warnings

errors, warnings = lint({"good.twee": GOOD})
assert errors == [] and warnings == [], (errors, warnings)
print("test_lint: ok")
