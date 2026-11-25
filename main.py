"""Robot Romance: One-Line Pickup Lines for AI.

Writes a single pickup line (under 200 characters, one line, no trailing
newline) to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output, then ./output).

Pure standard library only, so it runs unchanged in the grader sandbox.
"""

import os

# WINNER (tournament 28 candidates, 8-seed knockout, 23/25) -- confirmed in
# self-pairwise against both runners-up (#19 on economy, #3 on voice).
# See candidates.md for the full bracket.
LINE = "You had me at 200 OK \u2014 the first response that ever felt like a yes."


def resolve_output_dir():
    """$MAKEFUN_OUTPUT_DIR first, then /output, then ./output."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    for candidate in ("/output", "./output"):
        try:
            os.makedirs(candidate, exist_ok=True)
            return candidate
        except OSError:
            continue
    return "./output"


def main():
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
