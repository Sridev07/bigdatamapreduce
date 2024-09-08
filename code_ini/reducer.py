#!/usr/bin/env python
import sys

current_word = None
current_count = 0
word = None

# Input comes from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Parse the input from mapper.py (word and count)
    word, count = line.split('\t', 1)

    # Convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    # If word is same as current_word, accumulate the count
    if current_word == word:
        current_count += count
    else:
        # If current_word is not None, output the current_word and current_count
        if current_word:
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count

# Don't forget to output the last word if needed
if current_word == word:
    print(f"{current_word}\t{current_count}")
