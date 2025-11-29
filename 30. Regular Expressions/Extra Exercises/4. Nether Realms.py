import re

demon_names = input().split(',')

def calculate_health(name):
    # Sum ASCII codes of all characters except digits, +, -, *, /, and .
    health = 0
    for char in name:
        if char not in '0123456789+-*/.':
            health += ord(char)
    return health


def calculate_damage(name):
    # Extract all numbers with their signs
    numbers = re.findall(r'[+-]?\d+\.?\d*', name)
    base_damage = sum(float(num) for num in numbers)

    # Apply multiplication and division in order
    multipliers = re.findall(r'[*/]', name)
    for op in multipliers:
        if op == '*':
            base_damage *= 2
        else:  # op == '/'
            base_damage /= 2

    return float(base_damage)


# Calculate health and damage for each demon
demons = []
for name in demon_names:
    name = name.strip()
    health = calculate_health(name)
    damage = calculate_damage(name)
    demons.append((name, health, damage))

# Sort alphabetically by name
demons.sort(key=lambda x: x[0])

# Print results
for name, health, damage in demons:
    print(f"{name} - {health} health, {damage:.2f} damage")