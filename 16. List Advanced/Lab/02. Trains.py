nr_wagons = int(input())
train = list(0 for i in range(nr_wagons))
command = list(input().split())

while "End" not in command:
    if 'add' in command:
        people = int(command[1])
        train[len(train) - 1] += people
    elif 'insert' in command:
        wagon = int(command[1])
        people = int(command[2])
        train[wagon] += people
    elif 'leave' in command:
        wagon = int(command[1])
        people = int(command[2])
        train[wagon] -= people

    command = list(input().split())

print(train)
