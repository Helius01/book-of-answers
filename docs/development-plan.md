# Development plan

Source: the "Development plan" tab of the Claude Docs doc "The Book of Answers — Text Adventure Storyline" (2026-11-20). Checkboxes and the [Progress](#progress) section show the state of this repo. Story content: [storyline.md](storyline.md).

## Progress

Last updated 2026-11-20. Commits: `c8c5849` (Phases 0–1), `4c87c4d` (Phase 2), `82e8861` (Phase 3 polish), `6b742ea` (Phase 4 setup).

| Phase | Status |
| --- | --- |
| 0 — Setup | Done |
| 1 — Vertical slice (Acts 1–2) | Done. The playtest gate was **skipped on purpose** |
| 2 — Full content (Acts 3–7) | Done, including all 5 endings |
| 3 — Endings and polish | Done, except optional ambient sound. Codex journal, heartbeat lines, timers with a setting, and parchment style are in |
| 4 — Playtest and release | Started. Playtest build and guide, word-level check and itch.io package are ready. Playtests, wax tuning and the upload need a person |

**How to run:** `make build` gives the release `dist/index.html`. `make dev` gives `dist/dev.html`, with a debug panel that jumps to any act and sets Heart, Trust and wax. `make playtest` gives `dist/playtest.html`: no debug panel, but the run numbers show at each ending. `make package` zips the release for itch.io. `make lint` runs the story checker, and `make test` checks the checker.

**Live build:** <https://helius01.github.io/book-of-answers/> — GitHub Pages builds `master` on every push.

### Wax measured in scripted playthroughs

| Run | Wax at end of each act (A2 → A6) | Wax at final choice | Outcome |
| --- | --- | --- | --- |
| Honest, solves every puzzle, uses map, gives Rook the mirror | 91 · 100 · 87 · 88 · 65 | 49 | All four final choices, secret ending included |
| Careful, keeps the mirror, takes long roads | 86 · 95 · 72 · 73 · 50 | 35 | Truth / Gift / Keep |
| Lies everywhere, skips optional puzzles | 91 · 81 · 58 · 40 · 17 | 4 | Heart 2, only Ashes |

The plan targets about 15 wax for careful play. The game is still **too easy**. Tune it in Phase 4 with real players; the main controls are the `<<spend>>` values at the top of each `A#_start`.

### Changes from this plan

- **Broken links:** Tweego does *not* report them. `scripts/lint.py` checks them, plus dead ends, variables not set in `StoryInit`, duplicate passages, flag typos, and the writing rules (passages > 120 words, sentences > 12 words).
- **Act 1 wax:** the candle is lit in Act 2, so Act 1 costs no wax. The long road instead wets the wick, which costs 5 wax when the candle is lit.
- **Act 2 order:** the candle is lit *before* Tomasso (the church is dark inside), not after.
- **Darkness:** when wax reaches 0 before Act 7, the act restarts with 30 wax. In Act 7 it goes to the Ashes ending.
- **No undo:** `Config.history.maxStates = 1`, so the Back button is gone.
- **Autosave:** SugarCube 2.37 deprecated `Config.saves.autosave`. Passages tagged `autosave` call `Save.browser.auto.save()` instead.
- **Puzzle widgets:** `<<check guess "a|b" ok fail>>` for riddles. `<<mirror>>` works the same way and also counts toward the secret ending. The wrong-answer passage spends the 3 wax.
- **Items:**
  - Tunnel map: from the graveyard route; a shortcut in Act 4.
  - Flint: from the window route; relights the candle in Act 6.
  - Bird key: behind the angel lock in Act 3.
  - Sleeping water and +20 wax: hidden in the Act 5 mirror room.
  - Wings: a scripted box at the top of the tower, not a satchel item, so a full satchel can never block the escape.
  - Bell rope: one of the three Act 6 climbs, not an item.
- **Mirror puzzles (4):** A1 `MIDNIGHT`, A4 `TIME REVEALS`, A5 the ladder in the mirror floor, A6 `LOVE`. The optional ones (A4, A5) have a "Give up" link.
- **Book Speaks answers:** dark (A2), dreams (A3), time (A4), free (A5), love (A6).
- **Captive (end of Act 5):** Rook if his trust is below 4, otherwise Elena.
- **Act 7 Heart sources:** forgive the Abbot (+1), look at him in Leonardo's mirror (+1).
- **Act 7 rescue:**
  - Words: work with Heart ≥ 6.
  - Sleeping water: always works, but costs −1 Heart.
  - Help from an ally: Tomasso's trust ≥ 7, or Rook's trust ≥ 7 if Elena is the captive.
- **Final choice gates** (`A7_choice`):
  - Heart < 3: Ashes.
  - Release all (Truth): Heart ≥ 8 and captive saved.
  - Share safe pages (Gift): Heart ≥ 6.
  - Keep the book (New Abbot): always available.
  - Secret: 4 mirror puzzles and all trust ≥ 7.
- **SugarCube link text** drops a one-word `Word:` prefix (`[[Lie: "..."]]` shows only the quote). Write "Lie to him:" instead.
- **Open questions:** the defaults are used. Typed and choice puzzles, fixed hero Luca, web only, solo.

## Tech stack

Recommendation: build version 1 in **Twine with the SugarCube story format**, publish it as a single HTML file, and move to Ink only if the game later needs a real game engine.

| Option | Good for | Limits | Fit for this game |
| --- | --- | --- | --- |
| **Twine + SugarCube** | Choice-based stories, variables, inventory, timers, typed input, save slots, CSS styling | Large stories get messy without naming rules | Best for v1: every system in the story maps to a built-in feature |
| **Ink (+ inkjs in a web page)** | Large branching scripts, clean text files in Git, export to Unity | Timers, typed input and UI need your own code | Good for v2 or a mobile/Steam version |
| **Custom web app (TypeScript + JSON scenes)** | Full control of UI, sound, animation | You build saves, state and tools yourself | Only if you want a polished product from day one |
| **Inform 7** | Typed-command (parser) games | Hard for intermediate English players | Not recommended |

**Supporting tools:** Git for version control (Twine can export to Twee text files with Tweego), a spreadsheet to track variables and wax costs, itch.io for free web publishing.

*In this repo:* Tweego 2.1.1 and SugarCube 2.37.3 (vendored in `.storyformats/`). Twee files are written by hand; the Twine editor is not used.

## Roadmap

Five phases, four gates (the doc shows this as a diagram):

0. **Setup** → gate: build and lint green, UI frame works.
1. **Vertical slice (Acts 1–2)** → gate: playtest with 3–5 intermediate English players.
2. **Full content (Acts 3–7)** → gate: every act plays through, lint clean.
3. **Endings and polish** → gate: every ending condition tested.
4. **Playtest and release.**

Each phase ends at a gate. Do not start the next phase until the gate passes, especially Phase 1: a playable slice proves the systems work before you write 5 more acts.

## Game state

The whole game runs on 10 variables. Define them once in `StoryInit` and change them only through small helper widgets, so the rules stay in one place.

| Variable | Type / range | Start | Changed by | Read by |
| --- | --- | --- | --- | --- |
| `$wax` | number, 0–100 | 100 | Every action (`<<spend>>` widget); spare wax items | Darkness event at 0; Ashes ending |
| `$heart` | number, 0–10 | 5 | Honest / kind choices +1, lies / theft −1 | Love page (6+), endings (3, 6, 8) |
| `$trust` | object `{elena, tomasso, rook}`, each 0–10 | 5 each | Truth, help, broken promises | Act 4 Rook choice, Act 7 rescue, betrayal in Act 5 |
| `$satchel` | array of item ids, max 6 | `[]` | Pick up / drop scenes | Puzzle passages, Act 6 escape |
| `$mirrorSolved` | number, 0–N | 0 | Each solved mirror puzzle | Secret ending |
| `$answers` | array of answer ids | `[]` | "The Book Speaks" moments | Codex journal |
| `$clues` | array of clue ids | `[]` | `<<clue>>` at each discovery | Codex journal |
| `$act` | number, 1–7 | 1 | Act hub passages | Save slot names, journal |
| `$captive` | string | `""` | End of Act 5 (Elena or Rook) | Acts 6–7 text |
| `$flags` | object of true/false | `{}` | One-off events (`fire_seen`, `lied_tomasso`…) | Small text changes |

Rule of thumb: if a choice only changes one later sentence, use a flag. If it changes how a scene plays, use a score.

## Story structure

Use a **branch-and-merge** structure: choices split the path inside an act, but every act ends at one shared passage. Choices live on as variables, not as separate storylines. This keeps 5 endings possible without writing 5 full games.

**Passage naming:** `A3_painting`, `A3_painting_hide`, `A3_end`. Prefix = act, so the Twine map stays readable and Tweego files sort cleanly.

**One file per act** in Twee format (`act1.twee` … `act7.twee`), plus `systems.twee` for widgets, `ui.twee` for the candle bar and satchel, and `story.css`.

**Each act follows the same template:**

1. `A#_start` — sets `$act`, shows the vivid opening text.
2. 2–3 mission passages, each ending with 2–3 links.
3. One puzzle passage with typed input (`<<textbox>>`) or a choice grid.
4. One big choice that changes a score.
5. `A#_end` — the cliffhanger, auto-save, link to the next act.

**Reusable widgets** to write once in `systems.twee`: `<<spend n>>` (wax), `<<heart n>>`, `<<trust who n>>`, `<<give item>>` / `<<take item>>` (with the 6-item limit), `<<mirror answer>>` (checks a reversed word, ignores case and spaces), `<<speak id>>` (unlocks a "Book Speaks" answer), `<<clue id>>` (adds a page to the journal), and `<<hurry passage>>` (ten seconds to choose, if timers are on).

**Text style in code:** keep each passage under ~120 words. Long scenes split into short passages with a single "Continue" link, so the player reads one screen at a time.

## Candle budget

Starting numbers: a careful player finishes with about 15 wax, a careless one runs out in Act 6 or 7. Tune these after the first playtests.

**Cost per action**

| Action | Wax |
| --- | --- |
| Look, read, talk | 1 |
| Move to a new place | 2 |
| Wrong puzzle answer | 3 |
| Run / chase scene | 4 |
| Hide (`wait`) | 1 per turn |

**Budget per act** (the candle is lit in Act 2, so Act 1 costs nothing)

| Act | Planned spend | Wax found | Where it is found | Left after act (careful play) |
| --- | --- | --- | --- | --- |
| 2 — Church | 15 | 0 | — | 85 |
| 3 — Painting | 20 | +20 | Elena gives spare wax if trust is 5+ | 85 |
| 4 — Crypt | 30 | 0 | — | 55 |
| 5 — Library | 20 | +20 | Hidden in the mirror room | 55 |
| 6 — Bell Tower | 25 | 0 | — | 30 |
| 7 — Last Bell | 15 | 0 | — | 15 |

Show the candle as a bar that shrinks, and change the text at 50, 25 and 10 wax so the player feels it without reading numbers.

*Measured so far:* see [Wax measured in scripted playthroughs](#wax-measured-in-scripted-playthroughs). Careful play currently ends far above 15.

## Tasks by phase

### Phase 0 — Setup

- [x] Install Twine 2 and Tweego; create a Git repo with the folder layout from Story structure *(Tweego only, no Twine editor)*
- [x] Write `StoryInit` with all 9 variables
- [x] Write the helper widgets (`spend`, `heart`, `trust`, `give`/`take`, `mirror`, `speak`) *(plus `check` for riddles)*
- [x] Build the UI frame: candle bar, satchel panel, journal button, save/load

### Phase 1 — Vertical slice (Acts 1–2)

- [x] Write and build Act 1 (letter, chase, workshop, fire)
- [x] Write and build Act 2 (church entry, Tomasso's riddles, first candle)
- [x] One mirror puzzle and one riddle working end to end
- [x] Play it start to finish; check every link and every score change *(scripted browser playthrough)*

### Phase 2 — Full content (Acts 3–7)

- [x] Act 3: painting, Elena, angel number lock
- [x] Act 4: hiding with `wait`, Bridge of Names, Rook's offer
- [x] Act 5: mirror library, glowing page question, captive scene
- [x] Act 6: tower climb, bird key, love page with the Heart check
- [x] Act 7: the Abbot's story, rescue options, final choice
- [x] A way to raise Heart in Act 7 so the love page can still be unlocked *(forgive, mirror)*

### Phase 3 — Endings and polish

- [x] Write all 5 endings and test the conditions for each *(each one reached in a scripted run)*
- [x] Codex journal page (clues, maps, "Book Speaks" answers) *(Journal shows both: `$clues`, with the tunnel map as text, and the answers)*
- [x] Heartbeat lines and optional 10-second timers (with a setting to turn timers off) *(Act 1 chase; "Timers: on/off" in the story menu)*
- [x] Style: parchment look, candle-flicker effect, readable font size *(serif, parchment page, flicker; animation off under reduced motion)*
- [ ] Optional: ambient sound (rain, bells, keys) *(not started: needs audio files)*

### Phase 4 — Playtest and release

- [ ] Playtest rounds (see Testing) *(kit ready: [playtest.md](playtest.md); needs 5–10 players)*
- [ ] Rebalance wax and score thresholds *(waits for the playtest table; scripted careful play still ends near 35 wax)*
- [x] English check: sentence length and word level *(sentence length enforced by lint; word level checked by hand — long words are common, "notebooks" and "frightened" simplified)*
- [ ] Publish the HTML build on itch.io *(Pages test build is live; `make package` builds the itch zip, the upload needs the account)*

**Publishing steps**

1. `make package` → `dist/book-of-answers.zip`, with `index.html` at the root.
2. On itch.io, create a project with kind **HTML**, upload the zip, and tick *This file will be played in the browser*.
3. Set the viewport (1280×720 is a safe default), then check the phone layout before you tick *Mobile friendly*.
4. From the command line, `butler push build <user>/<game>:html` does the same upload. Install butler first.

**Free test URL (GitHub Pages)**

`.github/workflows/pages.yml` builds the release on every push to `master` and publishes it. Nothing to install on the runner: the workflow downloads Tweego.

This is already set up for the repo [Helius01/book-of-answers](https://github.com/Helius01/book-of-answers): <https://helius01.github.io/book-of-answers/>.

1. Push the repo to GitHub. Pages on a public repo is free; a private repo needs a paid plan.
2. Repo → Settings → Pages → Source: **GitHub Actions**.
3. Push to `master`, or run the workflow from the Actions tab.

If you rename the branch, add the new name to the `github-pages` environment (Settings → Environments → github-pages → deployment branches). The environment only allows branches on that list, and a blocked branch fails the job before its first step.

Vercel can host it too, but it needs the same Tweego download in a build command. One deploy path is enough. Saves live in the browser per site, so a player's run on the Pages URL does not share saves with `localhost` or itch.io.

### Phase 5 — not planned

The storyline has sequel hooks (the second volume in Egypt) and bonus ideas (Leonardo's machines). They are not scheduled.

## Testing

Test in three layers: automatic checks on every build, a debug panel for you, and real players at the end of Phases 1 and 4.

**Automatic checks (each build)**

- ~~Broken links: Tweego build fails or warns on missing passages.~~ Tweego does not; `scripts/lint.py` does.
- A small script that parses the Twee files and lists any passage with no way out, and any variable used but never set in `StoryInit`. *(Done: `make lint`, self-checked by `make test`.)*

**Debug panel (dev builds only)**

- Shows all variables live; buttons to jump to any act and set Heart, Trust and wax. *(Done: `debug/debug.twee`.)*
- Lets you check every ending condition in minutes instead of replaying.

**Playtests**

- After Phase 1: 3–5 players with intermediate English. Watch them play; note every word they ask about and every place they get stuck. *(Skipped.)*
- After Phase 4 content: 5–10 players. Record: final wax, Heart, ending reached, time to finish, and the moment they found most exciting. *([playtest.md](playtest.md) has the build, script and table.)*
- Success targets: most players finish; nobody runs out of wax before Act 5 on a first try; at least 3 different endings reached across the group.

## Open questions

Defaults used so far are in brackets.

- [ ] Choice-based only, or typed answers for puzzles too? (Plan assumes both.) *[both]*
- [ ] Fixed hero (Luca) or player picks name and gender? *[fixed Luca]*
- [ ] Web only, or mobile / Steam later? (Decides Twine vs Ink.) *[web]*
- [ ] Solo project or a team? Who writes, who builds, who tests? *[solo]*
- [ ] Target release date, to turn the phases into a dated timeline.
- [ ] Free game, or paid?
