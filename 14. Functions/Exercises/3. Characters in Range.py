def string_in_range(char1, char2):
    start = ord(char1) + 1
    end = ord(char2)
    return ' '.join(chr(i) for i in range(start, end))

char1 = input()
char2 = input()
result = string_in_range(char1, char2)
print(result)
