fire_cells = list(input().split('#'))
water = int(input())

valid_ranges = {
    "High": range(81, 126),
    "Medium": range(51, 81),
    "Low": range(1, 51)
}

put_out_cells = []
effort = 0
total_fire = 0

for cell in fire_cells:
    type_and_value = cell.split(" = ")
    if len(type_and_value) != 2:
        continue
    fire_type, value = type_and_value
    value = int(value)
    if value in valid_ranges.get(fire_type, []):
        if water >= value:
            water -= value
            put_out_cells.append(value)
            effort += value * 0.25
            total_fire += value

print("Cells:")
for cell in put_out_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
