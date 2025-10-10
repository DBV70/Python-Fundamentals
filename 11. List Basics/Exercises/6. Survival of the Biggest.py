numbers = list(map(int, input().split()))
n = int(input())

for each in range(n):
    numbers.remove(min(numbers))

print(', '.join(map(str, numbers)))
