import re


pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"
numbers = input()
valid_numbers = [i.group() for i in re.finditer(pattern, numbers)]

print(", ".join(valid_numbers))