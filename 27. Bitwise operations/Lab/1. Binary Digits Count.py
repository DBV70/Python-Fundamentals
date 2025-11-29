n = int(input())
b = input()
b_count = 0

n_binary = bin(n)[2:]

for _ in n_binary:
    if _ == b:
        b_count += 1

print(b_count)
