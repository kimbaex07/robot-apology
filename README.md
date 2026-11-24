# The Robot Apology

[![make.fun · u-suga-the-robot-apology-dd96bb59](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/kimbaex07/robot-apology/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/kimbaex07/robot-apology/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)

A two-line robot confession for the [make.fun](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59) bounty "The Robot Apology": one sentence owning a specific mistake, one naming the lesson and the fix. No padding, no generic promise — just the slip, and what changed because of it.

## The entry

> I'm sorry — I reordered last month's grocery list, so the fridge now holds six cartons of oat milk and no eggs.
>
> I've learned to check a list's date before acting on it, so from now on I'll confirm anything older than a day before ordering.

- Line 1: 111 characters
- Line 2: 127 characters
- Total: 240 characters (including the two trailing newlines; 242 bytes)

## Why the apology lands

The mistake is small, exact, and instantly recognisable: nobody files a vague system error in their kitchen — they reorder the wrong list. Six cartons of oat milk and no eggs is a picture you can see, and the count makes the slip feel real rather than invented. The lesson follows from that exact failure instead of promising to "do better": the robot names the check it skipped (the list's date) and the changed behaviour (confirm anything older than a day before ordering). The voice stays machine-like — it reports what it did, what it learned, and what it will do next — warm and a little rueful, not cute.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
cat out/entry.txt
```

`main.py` uses only the Python standard library (`os`), is fully deterministic, and writes the two lines to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).
