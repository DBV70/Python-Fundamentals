n = int(input())
acc_volume = 0

for i in range(n):
    pour_volume = int(input())
    acc_volume += pour_volume
    if acc_volume > 255:
        print('Insufficient capacity!')
        acc_volume -= pour_volume
print(acc_volume)
