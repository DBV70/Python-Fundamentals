def travel(current_distance:int, current_fuel:int):
    current_fuel -= current_distance
    if current_fuel >= 0:
        print(f"The spaceship travelled {current_distance} light-years.")
    else:
        print(f"Mission failed.")
    return current_fuel

def enemy(enemy_points:int, current_ammunition:int, current_fuel:int):
    if current_ammunition >= enemy_points:
        current_ammunition -= enemy_points
        print(f"An enemy with {enemy_points} armour is defeated.")
    else:
        current_fuel -= enemy_points * 2
        if current_fuel >= 0:
            print(f"An enemy with {enemy_points} armour is outmaneuvered.")
        else:
            print(f"Mission failed.")
    return current_ammunition, current_fuel

def repair(current_amount:int, current_ammunition:int, current_fuel:int):
    current_fuel += current_amount
    current_ammunition += current_amount * 2
    print(f"Ammunitions added: {current_amount * 2}.")
    print(f"Fuel added: {current_amount}.")
    return current_ammunition, current_fuel

travel_route = input().split("||")
fuel = int(input())
ammunition = int(input())

for each in travel_route:
    current_route = each.split(" ")
    if current_route[0] == "Travel":
        distance = int(current_route[1])
        fuel = travel(int(distance), fuel)
        if fuel < 0:
            break
    if current_route[0] == "Enemy":
        enemy_armor = int(current_route[1])
        ammunition, fuel =enemy(enemy_armor, ammunition, fuel)
        if fuel < 0:
            break
    if current_route[0] == "Repair":
        amount = int(current_route[1])
        ammunition, fuel = repair(amount, ammunition, fuel)
    if current_route[0] == "Titan":
        print("You have reached Titan, all passengers are safe.")
