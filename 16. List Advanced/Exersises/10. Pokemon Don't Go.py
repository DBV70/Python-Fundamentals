sequence = [int(num) for num in input().split()]
total_removed = 0

while len(sequence) > 0:
    index = int(input())
    if index < 0:
        removed_element = sequence[0]
        sequence[0] = sequence[-1]
    elif index >= len(sequence):
        removed_element = sequence[-1]
        sequence[-1] = sequence[0]
    else:
        removed_element = sequence.pop(index)

    total_removed += removed_element
    sequence = [each + removed_element if each <= removed_element else each - removed_element for each in sequence ]

print(total_removed)
