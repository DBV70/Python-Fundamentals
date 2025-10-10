key = int(input())
n = int(input())
message = ''

for i in range(n):
    chars = input()
    for char in chars:
        message += chr(ord(char) + key)

print(message)