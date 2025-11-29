first_char = ord(input())
second_char = ord(input())
text = input()

start = min(first_char, second_char)
end = max(first_char, second_char)

result = 0
for char in text:
    ascii_value = ord(char)
    if start < ascii_value < end:
        result += ascii_value

print(result)
