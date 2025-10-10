gifts = list(input().split())
command = list(input().split())

while True:
    if "OutOfStock" in command:
        gifts = ['None' if gift == command[1] else gift for gift in gifts]
    if "Required" in command:
        if int(command[2]) in range(len(gifts)):
            gifts[int(command[2])] = command[1]
    if "JustInCase" in command:
        gifts[len(gifts) - 1] = command[1]
    command.clear()
    command = list(input().split())
    if "No" in command and "Money" in command:
        break

gifts = [gift for gift in gifts if gift != 'None']

print(' '.join(map(str, gifts)))
