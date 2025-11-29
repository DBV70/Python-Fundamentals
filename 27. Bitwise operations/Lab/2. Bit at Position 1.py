n = int(input())
n_binary = bin(n)[2:]

bitAtPosition1 = (n >> 1) & 1
print(bitAtPosition1)
