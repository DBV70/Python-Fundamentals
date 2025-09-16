qty = int(input())
days_left = int(input())
spirit = 0
budget = 0
if days_left % 10 == 0:
    spirit -= 30

for i in range(days_left, 0, -1):
    if i % 2 == 0:
        budget += qty * 2
        spirit += 5
    if i % 3 == 0:
        budget += qty * 5 + qty * 3
        spirit += 3 + 10
    if i % 5 == 0:
        budget += qty * 15
        spirit += 17
        if i % 3 == 0:
            spirit += 30
    if i % 10 == 0:
        spirit -= 20
        budget += 23
    if i % 11 == 0:
        qty += 2

print(f'Total cost: {budget}')
print(f'Total spirit: {spirit}')
