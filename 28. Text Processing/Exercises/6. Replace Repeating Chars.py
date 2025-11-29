text = input()
result = ""

for char in text:
    if not result or result[-1] != char:
        result += char

print(result)