n = int(input())
field = []
destroyed_ships = 0

for _ in range(n):
    row = [int(x) for x in input().split()]
    field.append(row)

attacks = input().split()

for attack in attacks:
    row, col = [int(x) for x in attack.split('-')]
    if field[row][col] > 0:
        field[row][col] -= 1
        if field[row][col] == 0:
            destroyed_ships += 1

print(destroyed_ships)
