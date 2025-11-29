def contains(some_activation_key:str, some_command:list) -> str:
    substring = some_command[1]
    if substring in some_activation_key:
        return f"{some_activation_key} contains {substring}"
    else:
        return f"Substring not found!"

#Changes the substring between the given indices (the end index is exclusive) to upper or lower case
def flip(some_activation_key:str, some_command:list) -> str:
    upper_or_lower = some_command[1]
    start_index, end_index = int(some_command[2]), int(some_command[3])
    substring = some_activation_key[start_index:end_index]
    if upper_or_lower == "Upper":
        substring = substring.upper()
    elif upper_or_lower == "Lower":
        substring = substring.lower()
    some_activation_key = some_activation_key[:start_index] + substring + some_activation_key[end_index:]
    return some_activation_key

#Deletes the characters between the start and end indices (the end index is exclusive)
def slice(some_activation_key:str, some_command:list) -> str:
    start_index, end_index = int(some_command[1]), int(some_command[2])
    some_activation_key = some_activation_key[:start_index] + some_activation_key[end_index:]
    return some_activation_key

activation_key = input()
command = input()

while command != "Generate":
    command = command.split(">>>")
    action = command[0]
    if action == "Contains":
        print(contains(activation_key, command))
    elif action == "Flip":
        activation_key = flip(activation_key, command)
        print(activation_key)
    elif action == "Slice":
        activation_key = slice(activation_key, command)
        print(activation_key)
    command = input()

print(f"Your activation key is: {activation_key}")