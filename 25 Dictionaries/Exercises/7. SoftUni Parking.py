parking = {}

n = int(input())
for _ in range(n):
    command = input().split(' ')
    if 'register' in command:
        username, plate = command[1], command[2]
        if username not in parking:
            parking[username] = plate
            print(f"{username} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate}")

    if 'unregister' in command:
        username = command[1]
        if username in parking:
            print(f"{username} unregistered successfully")
            del parking[username]
        else:
            print(f"ERROR: user {username} not found")

for username, plate in parking.items():
    print(f"{username} => {plate}")