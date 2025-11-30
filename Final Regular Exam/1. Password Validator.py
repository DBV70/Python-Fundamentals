import re

def make_upper(current_password:str, current_command:list) -> str:
    index = int(current_command[2])
    if 0 <= index <= len(current_password) - 1:
        current_password = current_password[:index] + current_password[index].upper() + current_password[index + 1:]
    return current_password

def make_lower(current_password:str, current_command:list) -> str:
    index = int(current_command[2])
    if 0 <= index <= len(current_password) - 1:
        current_password = current_password[:index] + current_password[index].lower() + current_password[index + 1:]
    return current_password

def insert(current_password:str, current_command:list) -> str:
    index, symbol = int(current_command[1]), current_command[2]
    if 0 <= index <= len(current_password) - 1:
        current_password = current_password[:index] + symbol + current_password[index:]
    return current_password

def replace(current_password:str, current_command:list) -> str:
    symbol, value = current_command[1], int(current_command[2])
    if symbol in current_password:
        replacement = chr(ord(symbol) + value)
        current_password = current_password.replace(symbol, replacement)
    return current_password

def validation(current_password:str) -> bool:
    if len(current_password) < 8:
        print("Password must be at least 8 characters long!")
        return False
    elif not all(x.isalnum() or x == "_" for x in current_password):
    #elif not re.fullmatch(r'[a-z0-9_]+', current_password, re.IGNORECASE):
        print("Password must consist only of letters, digits and _!")
        return False
    elif not any(x.isupper() for x in current_password):
        print("Password must consist at least one uppercase letter!")
        return False
    elif not any(x.islower() for x in current_password):
        print("Password must consist at least one lowercase letter!")
        return False
    elif not any(x.isdigit() for x in current_password):
        print("Password must consist at least one digit!")
        return False
    else:
        return True

password = input()

while True:
    command = input().split()
    if command[0] == "Complete":
        break
    elif command[0] == "Make" and command[1] == "Upper":
        password = make_upper(password, command)
        print(password)
    elif command[0] == "Make" and command[1] == "Lower":
        password = make_lower(password, command)
        print(password)
    elif command[0] == "Insert":
        password = insert(password, command)
        print(password)
    elif command[0] == "Replace":
        password = replace(password, command)
        print(password)
    elif command[0] == "Validation":
        validation(password)
