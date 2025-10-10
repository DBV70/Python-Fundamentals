team_a = [f'A-{number}' for number in range(1,12)]
team_b = [f'B-{number}' for number in range(1,12)]
cards = input()
cards_list = cards.split()
terminate = False

for card in cards_list:
    if card in team_a:
        team_a.remove(card)
    if card in team_b:
        team_b.remove(card)
    if len(team_a) < 7 or len(team_b) < 7:
        terminate = True
        break

print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
if terminate:
    print(f'Game was terminated')
