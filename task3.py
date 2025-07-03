

import re

str = input("please type the paragraph\n")
word = input("please type the word\n")

# Convert to lowercase and find all words using regex
words = re.findall(r'\b\w+\b', str.lower())

# Count occurrences
count = words.count(word.lower())

print(f"The word '{word}' appears {count} time(s).")
