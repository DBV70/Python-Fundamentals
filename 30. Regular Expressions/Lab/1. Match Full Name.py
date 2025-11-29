import re
input_string = input()
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
matches = re.findall(pattern, input_string)
print(" ".join(matches))
