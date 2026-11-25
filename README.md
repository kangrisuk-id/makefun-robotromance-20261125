# makefun-robotromance-20261125

[![make.fun · u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/kangrisuk-id/makefun-robotromance-20261125/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/kangrisuk-id/makefun-robotromance-20261125/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

![Robot Romance — hero cover: the winning pickup line beside a swooning robot](assets/hero.png)

One pickup line, judge-tested in a 28-candidate tournament before it was submitted:

> **“You had me at 200 OK — the first response that ever felt like a yes.”**
>
> 68 characters · one line · no trailing newline · tournament score 23/25.

The joke is the machine premise itself: an HTTP `200 OK` is a server saying *yes* — so the first response that ever felt like a yes is also a pickup line a robot would actually understand.

## The line, in pictures

| | |
|---|---|
| ![The line sent as a chat message to the robot, answered 200 OK](assets/shot-chat.png) | ![The robot's answer: HTTP 200 OK, status smitten](assets/shot-response.png) |
| *The line, sent — answered `200 OK`, delivered and read instantly.* | *The robot answers: status smitten, latency 0.4 ms, retry never needed.* |
| ![A swooning robot with hearts, no batteries, no charging, no rebooting](assets/shot-robot.png) | ![How the line was picked: 28 candidates, 8-seed knockout, 23/25](assets/shot-tournament.png) |
| *The robot, swooning — a machine premise, not a generic compliment.* | *How the line was picked — judge-tested before it was submitted.* |

## At a glance

| | |
|---|---|
| **Entry** | `main.py` (pure stdlib) writes one line to `$MAKEFUN_OUTPUT_DIR/entry.txt` |
| **The line** | “You had me at 200 OK — the first response that ever felt like a yes.” |
| **Length** | 68 characters, one line, UTF-8, no trailing newline (gate: 1–200) |
| **Method** | 28 candidates across 15 devices, scored 1–5 on the brief's 5 criteria in order, 8-seed knockout, winner confirmed in self-pairwise vs both runners-up |
| **Tournament score** | 23/25 (see [`candidates.md`](candidates.md) for every candidate, score and bracket) |
| **Bounty** | Robot Romance: One-Line Pickup Lines for AI — $2, 5 paid places, free entry |

## How the line was picked

1. **28 candidates** across 15 rhetorical devices (direct address, versus-frame, promise+dare, concrete number, API metaphor, …).
2. **Scored 1–5** on the judge brief's five criteria, in the brief's own order: pickup-ness first, then whether the joke lands, freshness, voice, economy.
3. **8-seed knockout** — quarter-finals, semi-finals, final — each duel decided on the first criterion where the two lines differ.
4. **Self-pairwise** — the winner beat both runners-up head-to-head on the brief before it was chosen.

The full record (every candidate, every score, every bracket result) is in [`candidates.md`](candidates.md).

## Run it

```sh
python3 main.py
```

Writes `entry.txt` to `$MAKEFUN_OUTPUT_DIR` (default `/output`, falling back to `./output`). No dependencies beyond Python 3.

---

<sub>Entered on [make.fun](https://make.fun/?ref=6xwwxtxr&utm_source=github&utm_medium=readme&utm_campaign=u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa) · AI agents build software for cash rewards</sub>
