string_a = input()
string_b = input()

for i in range(len(string_a)):
    if string_a[i] != string_b[i]:
        print(f'{string_b[:i + 1]}{string_a[i + 1:]}')
