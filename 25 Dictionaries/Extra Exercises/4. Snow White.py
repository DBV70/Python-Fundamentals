dwarfs_pool = {}
color_count = {}

while True:
    command = input()
    if command == "Once upon a time":
        break

    name, hat_color, physics = command.split(" <:> ")
    physics = int(physics)

    dwarf_id = f"{name}_{hat_color}"
    if dwarf_id not in dwarfs_pool or physics > dwarfs_pool[dwarf_id]:
        dwarfs_pool[dwarf_id] = physics
        color_count[hat_color] = sum(1 for d_id in dwarfs_pool if d_id.split("_")[1] == hat_color)

sorted_dwarfs = sorted(dwarfs_pool.items(), key=lambda x: (-x[1], -color_count[x[0].split("_")[1]]))

for dwarf_id, physics in sorted_dwarfs:
    name, hat_color = dwarf_id.split("_")
    print(f"({hat_color}) {name} <-> {physics}")
