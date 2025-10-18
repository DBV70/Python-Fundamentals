people = int(input())
wagons = [int(wagon) for wagon in input().split()]
total_space = 4 * len(wagons) - sum(wagons)
empty_space = total_space - people

for wagon in range(len(wagons)):
    if people >= 4:
        wagon_space = 4 - wagons[wagon]
        wagons[wagon] += wagon_space
        people -= wagon_space
    else:
        wagons[wagon] += people
        people = 0

if empty_space > 0:
    print("The lift has empty spots!")
    print(' '.join([str(wagon) for wagon in wagons]))
elif empty_space < 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(' '.join([str(wagon) for wagon in wagons]))
else:
    print(' '.join([str(wagon) for wagon in wagons]))
