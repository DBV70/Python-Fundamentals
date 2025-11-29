numbers = input().split(' ')
result = 0

for number in numbers:
    result ^= int(number)

print(result)
