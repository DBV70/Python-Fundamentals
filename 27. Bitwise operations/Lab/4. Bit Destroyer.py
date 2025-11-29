n = int(input())
p = int(input())

mask = ~(1 << p)
newNumber = n & mask
print(newNumber)