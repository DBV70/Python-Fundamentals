factor = int(input())
count = int(input())
numbers = []
number = factor

while len(numbers) < count:
    if number % factor == 0:
        numbers.append(number)
    number += factor
print(numbers)
