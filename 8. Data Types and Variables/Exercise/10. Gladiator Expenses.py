lost_fights_count = int(input())
helmet_price = float(input())
swords_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expenses = 0.0
trashed_helmet = 0
trashed_swords = 0
trashed_shield = 0
trashed_armor = 0

for i in range(1, lost_fights_count + 1):
    if i % 2 == 0:
        trashed_helmet += 1
    if i % 3 == 0:
        trashed_swords += 1
    if i % 2 == 0 and i % 3 == 0:
        trashed_shield += 1
        if trashed_shield % 2 == 0:
            trashed_armor += 1

total_expenses = trashed_helmet * helmet_price + trashed_swords * swords_price + trashed_shield * shield_price + trashed_armor * armor_price
print(f'Gladiator expenses: {total_expenses:.2f} aureus')