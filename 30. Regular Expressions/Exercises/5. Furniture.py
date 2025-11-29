import re

bought_furniture = []
total_cost = 0
pattern = r">>([a-z]+)<<(\d+\.?\d*)!(\d+)"
command = input()
while command != "Purchase":
    match = re.search(pattern, command, re.IGNORECASE)
    if match:
        furniture_name, price, quantity = match.groups()
        bought_furniture.append(furniture_name)
        total_cost += float(price) * int(quantity)
    command = input()

print(f"Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")