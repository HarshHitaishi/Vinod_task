import re

str = input("enter the string\n")

# Use regex to find letter groups, digit groups, and symbol groups
# pattern = r'[a-zA-Z]+|\d+|[^a-zA-Z\d\s]+'
groups = re.findall(r'[a-zA-Z]+|\d+|[^a-zA-Z\d]+', str)

# Print each group on a new line
for group in groups:
    print(group)
