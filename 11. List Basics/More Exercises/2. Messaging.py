numbers = list(map(int, input().split()))
text = list(input())
message = []

for number in numbers:
    index = sum(map(int, str(number)))
    index = index % len(text)

    message.append(text.pop(index))

print(''.join(message))
