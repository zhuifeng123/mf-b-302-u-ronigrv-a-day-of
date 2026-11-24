import os

ENTRY = (
    "You don't need to learn a single line of code: describe your idea in plain English, "
    "and make.fun's AI agent builds you a real, working app you can share today."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    assert len(ENTRY) <= 240, len(ENTRY)
    assert "\n" not in ENTRY
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
