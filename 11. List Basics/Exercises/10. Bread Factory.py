energy = 100
coins = 100
working_day_events = input().split('|')
event_type_num = []
closed = False

for event in working_day_events:
    event_type_num = event.split('-')
    event_type, event_num = event_type_num
    event_num = int(event_num)
    if event_type == 'rest':
        initial_energy = energy
        energy += event_num
        if energy > 100:
            energy = 100
        print(f'You gained {energy - initial_energy} energy.')
        print(f'Current energy: {energy}.')
    elif event_type == 'order':
        if energy < 30:
            energy += 50
            print("You had to rest!")
        else:
            coins += event_num
            energy -= 30
            print(f'You earned {event_num} coins.')
    else:
        if event_num <= coins:
            coins -= event_num
            print(f'You bought {event_type}.')
        else:
            print(f'Closed! Cannot afford {event_type}.')
            closed = True
            break

if not closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
