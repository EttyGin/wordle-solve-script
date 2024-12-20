#!/usr/bin/env python3

import re

def find_matching_words(pattern, include, exclude) -> None:
    res: str = ""
    with open(r"/usr/share/dict/words", "r") as word_file:
        for line in word_file:
            word: str = line.strip().lower()
            if (
            re.match(f"^{pattern}$", word)
            and word.isalpha()
            and all(letter in word for letter in include)
            and all(letter not in word for letter in exclude)
        ):
                res += word + "\n"
    print(res)
    
if __name__ == "__main__":
    while True:
        pattern = input("Enter a pattern (or q to exit): ")
        if pattern.lower() == 'q':
            break
        include = input("Enter letters to include: ")
        exclude = input("Enter letters to exclude: ")
        find_matching_words(pattern, include, exclude)