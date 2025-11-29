def add(current_command:list, some_pieces:dict) -> dict:
    piece_, composer_, key_ = current_command[1], current_command[2], current_command[3]
    if piece_ not in some_pieces:
        some_pieces[piece_] = [composer_, key_]
        print(f"{piece_} by {composer_} in {key_} added to the collection!")
    else:
        print(f"{piece_} is already in the collection!")
    return some_pieces

def remove(current_command:list, some_pieces:dict) -> dict:
    piece_ = current_command[1]
    if piece_ in some_pieces:
        print(f"Successfully removed {piece_}!")
        del some_pieces[piece_]
    else:
        print(f"Invalid operation! {piece_} does not exist in the collection.")
    return some_pieces

def change_key(current_command:list, some_pieces:dict) -> dict:
    piece_, new_key = current_command[1], current_command[2]
    if piece_ in some_pieces:
        some_pieces[piece_][1] = new_key
        print(f"Changed the key of {piece_} to {new_key}!")
    else:
        print(f"Invalid operation! {piece_} does not exist in the collection.")
    return some_pieces

number_of_pieces = int(input())
pieces = {}

for i in range(number_of_pieces):
    piece, composer, key = input().split('|')
    pieces[piece] = [composer, key]

command = input()
while command != 'Stop':
    command = command.split('|')
    action = command[0]
    if action == 'Add':
        pieces = add(command, pieces)
    elif action == 'Remove':
        pieces = remove(command, pieces)
    elif action == 'ChangeKey':
        pieces = change_key(command, pieces)
    command = input()

for piece, info in pieces.items():
    composer, key = info
    print(f"{piece} -> Composer: {composer}, Key: {key}")
