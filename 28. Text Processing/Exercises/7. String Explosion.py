text = input()
result = ""
strength = 0

for index in range(len(text)):
    if strength > 0 and text[index] != ">":
        strength -= 1
    elif text[index] == ">":
        result += text[index]
        strength += int(text[index + 1])
    else:
        result += text[index]

print(result)