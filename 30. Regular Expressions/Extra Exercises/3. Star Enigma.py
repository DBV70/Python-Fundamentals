import re

n = int(input())
attacked = []
destroyed = []

pattern = re.compile(r"@(?P<name>[A-Za-z]+)[^@\-!:>]*:(?P<population>\d+)[^@\-!:>]*!(?P<attack>[AD])![^@\-!:>]*->(?P<soldiers>\d+)")

for _ in range(n):
    encrypted = input()
    shift = len(re.findall(r"[starSTAR]", encrypted))
    decrypted = "".join(chr(ord(c) - shift) for c in encrypted)

    match = pattern.search(decrypted)
    if not match:
        continue

    name = match.group("name")
    attack_type = match.group("attack")
    if attack_type == "A":
        attacked.append(name)
    else:
        destroyed.append(name)

attacked.sort()
destroyed.sort()

print(f"Attacked planets: {len(attacked)}")
for p in attacked:
    print(f"-> {p}")
print(f"Destroyed planets: {len(destroyed)}")
for p in destroyed:
    print(f"-> {p}")