# The Book of Answers — Text Adventure Storyline

Source: the "Tab 1" tab of the Claude Docs doc "The Book of Answers — Text Adventure Storyline" (2026-11-20). For what the game actually implements, see [development-plan.md](development-plan.md#progress); the code is in `src/`.

## Story overview

Florence, 1503. Leonardo da Vinci gives the player one secret job: find a lost book called *Human in the Matrix* and give its knowledge to the world before a secret brotherhood burns it.

**The book.** It was written long ago by an unknown hand. It explains how the world works, why people dream, what time really is, and the true meaning of the word "love". Its pages are blank to most people. They only show words in candlelight, and only to a reader with an honest heart.

**The place.** The book is hidden in the Church of the Silent Bells, an old church on a hill outside Florence. The bells have not rung for one hundred years. People say the church is empty. It is not.

**The enemy.** The Order of the Closed Eye is a secret group of rich and powerful men. They believe ordinary people are not ready for the truth. Knowledge is power, and they want to keep all of it.

**The hero's duty.** Leonardo is too old and too watched to go himself. He trusts the player, his young friend and student, with the mission.

**The big question of the game.** Should all knowledge be free? The player hears both sides and decides at the end.

### Writing rules for the game text

- Short sentences. Most under 12 words.
- Common words. "Big", not "enormous". "Afraid", not "apprehensive".
- Use the five senses in every scene: what the player sees, hears, smells, feels, and tastes.
- Use "you": *You touch the wall. It is cold and wet, like a fish.*
- End every scene with a hook: a sound, a shadow, a question.
- Give the player 2 or 3 clear choices, never more.

## Characters

| Character | Who they are | What the player feels |
| --- | --- | --- |
| **Luca Moretti** (the player) | 19 years old, a mapmaker and Leonardo's student. Fast hands, good memory, can read mirror writing. | "This is me." |
| **Leonardo da Vinci** | Old, tired, brilliant. He speaks in riddles because spies are everywhere. He sends coded letters and strange machines. | Trust, warmth, wonder |
| **Sister Elena** | A young nun who lives in the church in secret. She knows every tunnel. She lost her brother to the Order. | Hope, maybe love |
| **Tomasso the Blind** | An old bell-ringer. He cannot see, but he hears everything. He speaks only in questions. | Mystery, a little fear |
| **Rook** | A street thief, 14 years old, quick and funny. Sells information to anyone who pays. | Fun, but can you trust him? |
| **The Grey Abbot** | Leader of the Order of the Closed Eye. Calm, polite, never shouts. He believes he is protecting the world. | Cold fear, then doubt |
| **The Silent Ones** | The Order's hunters. Grey robes, masks without mouths. They never speak. You hear only their keys. | Pure fear |

**The twist.** The Grey Abbot was once Leonardo's best friend. They found the book together, forty years ago. Leonardo wanted to share it. The Abbot hid it. Their friendship broke that night, and the Abbot has a reason the player will not expect: in the final act, he says the book once drove a man mad.

## Game systems

Four simple systems keep the player tense and make every choice matter.

| System | How it works | Why it is exciting |
| --- | --- | --- |
| **The Candle** | The player carries one candle. It has 100 drops of wax. Every action uses wax. Running uses more. When it reaches 0, the player is in total darkness and the Silent Ones come. | A real clock the player can feel. Show it often: *Your candle is short now. The flame shakes.* |
| **Heart** | An honesty score from 0 to 10. Lying, stealing, and hurting people lower it. Helping people raises it. | The book's pages only show words to a high Heart. Bad choices make the ending harder. |
| **Trust** | Each ally (Elena, Tomasso, Rook) has a trust score. | High trust: they save you later. Low trust: they betray you. |
| **The Satchel** | The inventory. Holds 6 items only. | Hard choices: keep the rope or the mirror? |

**Key items:** Leonardo's mirror, a bronze key shaped like a bird, a map of the tunnels, flint and spare wax, a bell rope, a vial of "sleeping water", Leonardo's folding wings (Act 6 only).

**Mirror writing.** Many clues are written backwards, like Leonardo's real notebooks. The player must type the word the right way round to unlock it. Example: `EVOL` → `LOVE`.

## Stages and missions

The game has 7 acts. Each act has one goal, 2–3 missions, one puzzle, and one big choice. Every act ends on a cliffhanger.

### Act 1 — The Letter in the Bread

**Goal:** Get Leonardo's secret message without the spies seeing.

> *Night in Florence. Rain hits the roofs like small stones. You smell wet bread and smoke. A baker pushes a warm loaf into your hands. "From the old man," he whispers. Then he runs. You break the bread. Inside is a paper, folded tight. The words are backwards.*

**Missions**

1. Read the mirror letter (puzzle: reverse the words).
2. Lose the man in the red hat who follows you through the market.
3. Meet Leonardo in his workshop at midnight.

**Scene to remember:** Leonardo's workshop. Wooden wings hang from the ceiling like sleeping bats. He gives you a small mirror and says: *"The book does not lie. But people do. Trust the mirror, not the face."*

**Choice:** Pay Rook the thief to show a secret road (−Heart, +speed), or walk the long road in the rain (−wax).

**Cliffhanger:** When you leave, you hear a scream behind you. The workshop is on fire.

### Act 2 — The Church of the Silent Bells

**Goal:** Get inside the church alive.

> *The church stands on the hill like a black tooth. The doors are chained. Crows sit on the bell tower and watch you. Nobody is here. But the snow on the steps has fresh footprints. Going in. Not coming out.*

**Missions**

1. Find a way in: the chained door, the broken window, or the graveyard tunnel.
2. Meet Tomasso the Blind. Answer his three questions to pass. (*"What has a face but no eyes?"* — a clock.)
3. Light the first candle. Wax counter starts at 100.

**Choice:** Lie to Tomasso about who sent you (Trust drops), or tell the truth (he helps you later).

**Cliffhanger:** A bell rings. One time. Tomasso goes white. *"The bells have not rung in one hundred years,"* he whispers. *"They know you are here."*

### Act 3 — The Painting That Breathes

**Goal:** Find the first clue to the book's location.

> *A giant painting covers the wall. Angels with sad faces. As your candle moves, their eyes seem to move too. You come closer. You can hear something. Air. The painting is breathing.*

**Missions**

1. Discover the hidden room behind the painting (wind comes from behind it).
2. Meet Sister Elena, who points a knife at you first and asks questions later.
3. Solve the angels puzzle: each angel points to a number. Together they open a stone lock (code: the year Leonardo was born, 1452).

**Choice:** Tell Elena the full truth about the book, or keep it secret. Truth makes her an ally. Secret makes her suspicious.

**Cliffhanger:** Footsteps. Keys. Jingle, jingle. The Silent Ones are in the church.

### Act 4 — The Crypt of Whispers

**Goal:** Cross the underground tombs to the old library.

> *Stairs go down into the dark. The air is cold and tastes like old coins. Bones lie in the walls, neat as books on a shelf. Your candle makes the skulls smile.*

**Missions**

1. Hide from a Silent One. The player must type `wait` three times. Moving early means capture.
2. Cross the Bridge of Names: stones with names on them. Step only on the names of people who loved someone. Clues come from short sad stories carved on each tomb.
3. Find Leonardo's old drawing on the wall: a map with one missing piece.

**Choice:** Rook appears and offers to lead the Silent Ones away, but asks for your mirror. Give it (high risk, high reward) or say no.

**Cliffhanger:** The tunnel behind you collapses. You can only go forward. And something ahead is singing.

### Act 5 — The Library Upside Down

**Goal:** Find the room where the book is kept.

> *You enter a room and your stomach turns. The books are on the ceiling. The chairs are on the ceiling. A table hangs over your head with a cup of wine on it. The wine does not fall. Then you understand. It is not the room that is upside down. It is a mirror floor, smooth as ice.*

**Missions**

1. Solve the mirror room: only objects that appear in the reflection but not in the real room are clues.
2. Read a page torn from the book. It glows. It asks the player one question: *"What do you want more — to be right, or to be free?"* Their answer changes Heart.
3. Learn the truth: the book is in the Bell Tower, inside the biggest bell.

**Cliffhanger:** Elena (or Rook, if his trust is low) is caught. The Grey Abbot's voice fills the library: *"Bring me the book, Luca. Or your friend goes into the fire."*

### Act 6 — The Bell Tower

**Goal:** Climb the tower, reach the bell, and get the book.

> *The stairs go up and up. The wood cries under your feet. Wind screams through the holes in the walls. Below you, Florence is a field of tiny lights. Above you, the great bell waits, black and silent, like a sleeping giant.*

**Missions**

1. Climb with a broken staircase (choose: jump, use the bell rope, or climb the outside wall).
2. Open the bell with the bronze bird key.
3. Hold the book for the first time. It is warm, like a living thing. It opens by itself to the page about love.

**The page about love (shown only if Heart is 6 or more):**

> *Love is not a feeling. A feeling comes and goes like weather. Love is a choice you make again every morning. It is choosing someone's good over your own comfort. This is the oldest law of the world. Everything else is built on it.*

(If Heart is under 6, the page stays blank. The player must earn it back in Act 7.)

**Cliffhanger:** The Grey Abbot stands at the top of the stairs. Elena is beside him, tied. He smiles kindly. *"Now we talk."*

### Act 7 — The Last Bell

**Goal:** Decide the fate of the book.

> *The Abbot does not attack. He sits down. He looks tired, like Leonardo. "I was there when we found it," he says. "A man read the page about death. He never spoke again. Are you sure the world is ready?"*

**Missions**

1. Listen to the Abbot's story (the twist). The player can ask questions.
2. Free Elena: with words, with a trick (the sleeping water), or with help from an ally whose trust is high.
3. Make the final choice (see Endings).

**Final escape idea:** The Silent Ones come up the stairs. The only way out is Leonardo's folding wings. The player jumps from the tower and glides over Florence at sunrise, the book against their chest, the bells ringing behind them for the first time in one hundred years.

## Endings and bonus ideas

Five endings depend on the final choice, the Heart score, and ally trust. This makes players want to play again.

| Ending | How to get it | What happens |
| --- | --- | --- |
| **The Bells of Truth** (best) | Release the book, Heart 8+, Elena saved | The bells ring all over Italy. The book is copied by hand in a hundred cities. Leonardo smiles at his window. |
| **The Careful Gift** | Release only some pages, Heart 6+ | You share the page about love and keep the dangerous pages hidden. The Abbot nods. Two old friends forgive each other. |
| **The New Abbot** | Keep the book for yourself | The book's pages slowly go blank. You understand too late: knowledge kept in the dark dies. Your mask has no mouth. |
| **Ashes** | Candle reaches 0 in Act 7, or Heart under 3 | The Abbot burns the book. One page flies out the window. The final line: *Somewhere, a child picks up a glowing page…* |
| **The Secret Ending** | Solve every mirror puzzle and keep all trust high | The last page of the book has your name on it. It was written 300 years before you were born. |

### Bonus ideas to make it more exciting

- **Leonardo's machines:** small gadgets as rewards, like a clockwork bird that carries messages or a lantern that makes no shadow.
- **The Book Speaks:** once per act, the book (or its torn pages) whispers an answer to a big human question: *Why do we dream? What is time? Why do we fear the dark?* Players collect these answers like treasures.
- **Heartbeat lines:** when danger is near, short lines appear alone on the screen: *Thump. Thump. Thump.*
- **Timed scenes:** in chase scenes, give the player 10 seconds to choose.
- **A codex journal:** a page that fills with every clue, map, and answer the player finds.
- **Sequel hook:** the book has a second volume. It is hidden in Egypt.

How to build it: [Development plan](development-plan.md)
