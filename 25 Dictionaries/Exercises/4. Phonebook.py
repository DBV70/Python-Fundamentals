phonebook = {}

while True:
    command = input()
    if command.isdigit():
        to_search = int(command)
        break
    name, number = command.split("-")
    phonebook[name] = number

for _ in range(to_search):
    name = input()
    if name not in phonebook:
        print(f"Contact {name} does not exist.")
        continue
    print(f"{name} -> {phonebook[name]}")
