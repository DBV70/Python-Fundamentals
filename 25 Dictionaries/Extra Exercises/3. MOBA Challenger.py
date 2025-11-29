pool = {}

while True:
    command = input()
    if command == "Season end":
        break

    if "->" in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in pool:
            pool[player] = {}
        if position not in pool[player]:
            pool[player][position] = skill
        elif skill > pool[player][position]:
            pool[player][position] = skill

    if "vs" in command:
        player1, player2 = command.split(" vs ")
        if player1 in pool and player2 in pool:
            common_position = set(pool[player1].keys()).intersection(set(pool[player2].keys()))

            if common_position:
                if sum(pool[player1].values()) > sum(pool[player2].values()):
                    pool.pop(player2)
                elif sum(pool[player2].values()) > sum(pool[player1].values()):
                    pool.pop(player1)

for player, positions in sorted(pool.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{player}: {sum(positions.values())} skill")
    for position, skill in sorted(positions.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {position} <::> {skill}")