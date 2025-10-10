def tribonacci_sequence(n):
    seq = []
    for i in range(n):
        if i == 0:
            seq.append(1)
        elif i == 1:
            seq.append(1)
        elif i == 2:
            seq.append(2)
        else:
            seq.append(seq[i-1] + seq[i-2] + seq[i-3])
    print(' '.join(str(num) for num in seq))

n = int(input())
tribonacci_sequence(n)