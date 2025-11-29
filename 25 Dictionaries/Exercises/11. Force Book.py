force_book = {}

while True:
    command = input()
    if "Lumpawaroo" in command:
        break
    elif "|" in command:
        side, user = command.split(" | ")
        if side not in force_book:
            force_book[side] = []
        user_exists = False
        for _ in force_book:
            if user in force_book[_]:
                user_exists = True
                break
        if not user_exists:
            force_book[side].append(user)

    elif "->" in command:
        user, side = command.split(" -> ")
        if side not in force_book:
            force_book[side] = []
        for _ in force_book:
            if user in force_book[_]:
                force_book[_].remove(user)
                break
        force_book[side].append(user)
        print(f"{user} joins the {side} side!")

for side, users in force_book.items():
    if not users:
        continue
    print(f"Side: {side}, Members: {len(users)}")
    for user in users:
        print(f"! {user}")
