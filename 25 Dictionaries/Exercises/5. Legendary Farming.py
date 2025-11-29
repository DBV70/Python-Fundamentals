key_materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
junks = {}
legendary_obtained = False

while True:
    daily = input().split()
    for i in range(0, len(daily), 2):
        quantity = int(daily[i])
        material = daily[i + 1].lower()
        if material in key_materials:
            key_materials[material] += quantity
            if key_materials[material] >= 250:
                key_materials[material] -= 250
                legendary_material = material
                legendary_obtained = True
                break
        else:
            if material not in junks:
                junks[material] = 0
            junks[material] += quantity
    if legendary_obtained:
        break

print(f"{legendary[legendary_material]} obtained!")
print(f"shards: {key_materials.pop('shards')}")
print(f"fragments: {key_materials.pop('fragments')}")
print(f"motes: {key_materials.pop('motes')}")
for material, quantity in junks.items():
       print(f"{material}: {quantity}")
