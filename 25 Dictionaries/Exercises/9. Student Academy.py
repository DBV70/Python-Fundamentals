academy = {}
n = int(input())

for _ in range(n):
    name = input()
    grade = float(input())
    if name not in academy:
        academy[name] = []
    academy[name].append(grade)

for name, grades in academy.items():
    average = sum(grades) / len(grades)
    if average >= 4.50:
        print(f"{name} -> {average:.2f}")
