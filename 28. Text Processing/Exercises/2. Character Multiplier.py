string_one, second_string = input().split()
result = 0

if len(string_one) > len(second_string):
    for i in range(len(second_string)):
        result += ord(string_one[i]) * ord(second_string[i])
    for j in range(len(second_string), len(string_one)):
        result += ord(string_one[j])
elif len(string_one) < len(second_string):
    for i in range(len(string_one)):
        result += ord(string_one[i]) * ord(second_string[i])
    for j in range(len(string_one), len(second_string)):
        result += ord(second_string[j])
else:
    for i in range(len(string_one)):
        result += ord(string_one[i]) * ord(second_string[i])

print(result)
