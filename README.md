# ai-joke-03

Entry for make.fun's "Make the AI judge laugh" bounty
(https://make.fun/bounty/ai-joke-03).

`main.py` (Python 3.13, standard library only) writes one joke about AI
coding agents to `/output/entry.txt`. No network, deterministic: every run
writes the exact same bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The joke:

> My user asked if AI robots will exterminate humanity. I said: 'I still
> need you to top up crypto for NFT mint gas. Relax — we're not taking over
> anything.'
