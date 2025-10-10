n = int(input())
message = ''
brackets = 0

for i in range(n):
    chars = input()
    message += chars

for char in message:
    if char == '(':
        brackets += 1
    if char == ')':
        brackets -= 1
    if brackets > 1 or brackets <= -1:
        break

if brackets == 0:
    print('BALANCED')
else:
    print('UNBALANCED')
