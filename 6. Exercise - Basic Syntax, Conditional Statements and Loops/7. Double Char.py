string = input()

while string != 'End':
    if string != 'SoftUni':
        for char in string:
            print(f'{char}{char}', end='')
        print()
    string = input()
