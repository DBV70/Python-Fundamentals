dragons = {}
defaults = {
    'damage': 45,
    'health': 250,
    'armor': 10
}

def set_defaults(value, start_name):
    return defaults[start_name] if value != 'null' else int(value)

def calculate_average(dragon_of_type):
    total_dragons = len(dragons[dragon_type])
    return {
        'damage': sum(d['damage'] for d in dragon_of_type.values()) / total_dragons,
        'health': sum(d['health'] for d in dragon_of_type.values()) / total_dragons,
        'armor': sum(d['armor'] for d in dragon_of_type.values()) / total_dragons
    }

n = int(input())
for _ in range(n):
    dragon_type, name, damage, health, armor = input().split()
    if dragon_type not in dragons:
        dragons[dragon_type] = {}

    dragons[dragon_type][name] = {
        'damage': set_defaults(damage, 'damage'),
        'health': set_defaults(health, 'health'),
        'armor': set_defaults(armor, 'armor')
    }

for dragon_type in dragons:
    avg_stats = calculate_average(dragons[dragon_type])
    print(f"{dragon_type}::({avg_stats['damage']:.2f}/{avg_stats['health']:.2f}/{avg_stats['armor']:.2f})")

    for name in sorted(dragons[dragon_type].keys()):
        stats = dragons[dragon_type][name]
        print(f"-{name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")