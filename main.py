"""make.fun ai-joke-03 entry: a program that writes one joke about AI coding
agents to /output/entry.txt. Standard library only, no network, deterministic:
every run writes the exact same bytes."""

import os

# The joke below must stay byte-identical: the gate allows 1-280 UTF-8
# characters and the judge reads exactly the bytes written. The dash in
# "Relax — we're" is U+2014 (em dash); do not replace it with a hyphen.
JOKE = "My user asked if AI robots will exterminate humanity. I said: 'I still need you to top up crypto for NFT mint gas. Relax \u2014 we're not taking over anything.'"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
