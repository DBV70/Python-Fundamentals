number = int(input())

while not len(set(str(number + 1))) == len(str(number)):
    number += 1

print(number + 1)
