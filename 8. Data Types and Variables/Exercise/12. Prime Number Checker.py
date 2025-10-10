number = int(input())
x = 0

for i in range(2, number):
    if number % i == 0:
        x += 1

print(x == 0)
