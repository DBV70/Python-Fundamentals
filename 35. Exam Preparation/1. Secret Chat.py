message = input()

while True:
    command = input()
    if command == "Reveal":
        break

    command = command.split(":|:")
    action = command[0]

    if action == "InsertSpace":
        index = int(command[1])
        message = message[:index] + " " + message[index:]
    elif action == "Reverse":
        substring = command[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message = message + substring[::-1]
        else:
            print("error")
            continue
    elif action == "ChangeAll":
        substring, replacement = command[1], command[2]
        message = message.replace(substring, replacement)

    print(message)

print(f"You have a new text message: {message}")
