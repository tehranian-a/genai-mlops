import argparse
from collections import Counter
import re

def tokens(text):
    # split into words; make lowercase; keep letters/numbers/underscore/apostrophe
    return re.findall(r"[A-Za-z0-9_']+", text.lower())

def main():
    p = argparse.ArgumentParser(description="Count top words in a file")
    p.add_argument("--file", required=True, help="path to input text file")
    p.add_argument("--top", type=int, default=5, help="how many top words to show")
    args = p.parse_args()

    with open(args.file, "r", encoding="utf-8") as f:
        words = tokens(f.read())

    for w, c in Counter(words).most_common(args.top):
        print(f"{w}\t{c}")

if __name__ == "__main__":
    main()
