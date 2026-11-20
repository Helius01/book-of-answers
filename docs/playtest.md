# Playtest kit

Phase 4 of [development-plan.md](development-plan.md). The game has never been played by anyone else, so this round tests the whole thing: can a player finish, and where do they struggle?

## Build

```sh
make playtest                      # dist/playtest.html: release build + run numbers at each ending
python3 -m http.server -d dist 8000
```

Open `http://localhost:8000/playtest.html`. Do **not** use `dev.html`: its debug buttons let players jump ahead and change scores.

## Session script

Say this before they start, and little else after:

> This is a short choice-based story. It takes about 30 minutes. Your candle burns down as you act, and there are five endings. There are no wrong answers. Please think aloud if you can.

Rules for the facilitator:

- Do not help with puzzles, do not point at the candle, do not say "you missed a clue".
- Write down every word they ask about and every passage where they stop moving for more than a minute.
- If they ask "am I doing it right?", answer "what do you think?"
- One sitting per player. The autosave keeps their place, but a fresh start is the point.

## Record per player

The ending passage ends with a grey Playtest line: wax, Heart, Trust, mirror puzzles, clues, timers. Copy it before they close the tab.

| Player | Date | Minutes | Wax | Heart | Trust (E/T/R) | Ending | Stuck at | Words asked | Journal opened | Timers hit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |

Also ask at the end:

1. Which moment did you like most?
2. Did you understand what the candle was for?
3. Did you want to play again for another ending?

## Targets

From the plan:

- Most players finish on their first try.
- Nobody runs out of wax before Act 5.
- At least three different endings across the group.
- Careful play ends near 15 wax. The last scripted runs ended around 35, so this round is expected to say "too easy".

## Turning the data into a change

Only change numbers after the round, not during it.

- Spends live in `<<spend n>>` calls inside the acts; the big ones sit at the top of each `A#_start`.
- The two +20 wax finds are in `A3_end` (Elena) and `A5_shelf` (mirror room).
- Heart and Trust thresholds are in `A7_choice`, `A6_book` and `A7_rescue`.
- Re-run `make lint && make test`, then update the wax table in the plan.

## After the round

Fill in the table above, write one line under it for each change you decide, and tick the Phase 4 boxes in [development-plan.md](development-plan.md).
