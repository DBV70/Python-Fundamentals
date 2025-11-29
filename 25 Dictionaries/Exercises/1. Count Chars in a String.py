text = input()
charCount = {}
for char in text:
    if char != " ":
        if char in charCount:
            charCount[char] += 1
            continue
        else:
            charCount[char] = 1

for char in charCount:
    print(f"{char} -> {charCount[char]}")
