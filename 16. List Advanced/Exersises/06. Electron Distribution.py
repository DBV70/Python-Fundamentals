electrons = int(input())
shells = []
shell_number = 1

while electrons > 0:
    if electrons >= 2 * shell_number**2:
        shells.append(2 * shell_number**2)
    else:
        shells.append(electrons)

    electrons -= int(shells[shell_number -1])
    shell_number += 1

print(shells)
