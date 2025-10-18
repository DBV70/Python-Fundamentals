nr_rooms = int(input())
total_free_chairs = 0

for room in range(1, nr_rooms + 1):
    room_chairs, room_people = input().split()
    difference = len(room_chairs) - int(room_people)
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {room}")
    total_free_chairs += difference

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")
