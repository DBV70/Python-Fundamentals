qty = int(input())
days_left = int(input())
spirit = 0
budget = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        qty += 2
    if day % 2 == 0:
        budget += qty * 2
        spirit += 5
    if day % 3 == 0:
        budget += qty * 5 + qty * 3
        spirit += 3 + 10
    if day % 5 == 0:
        budget += qty * 15
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        budget += 23
    if (day == days_left) and day % 10 == 0:
        spirit -= 30

print(f'Total cost: {budget}')
print(f'Total spirit: {spirit}')
