# Office Laugh Line — Make the AI Judge Laugh

[![make.fun](https://img.shields.io/badge/make.fun-u--alfasurya91--make--the--ai--judge--laugh--6ed40225-blue)](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)

Entry for the [Make the AI Judge Laugh](https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225) bounty on make.fun: one office-life joke, one line, under 200 characters, judged pairwise by an AI judge on truth to office life, surprise of the turn, tightness, and freshness.

## The joke

> My badge opens every door in the building — except the one to the meeting I'm already late for.

95 characters, one line, one sentence. The badge is the one office object no competitor in the field's 281 visible titles jokes about — and the one door that matters is exactly the exception.

## How it works

`main.py` writes the joke to `$MAKEFUN_OUTPUT_DIR/entry.txt` (the grader mounts that directory at `/output`). Deterministic, no network, no dependencies.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Bounty

- Competition: https://make.fun/bounty/u-alfasurya91-make-the-ai-judge-laugh-6ed40225
- Harness: program/v1 — the program writes one text to `/output/entry.txt`
- Gate: UTF-8 text of 1 to 200 characters
