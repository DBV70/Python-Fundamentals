key = [int(num) for num in input().split()]
decrypted_text = ""

while True:
    encrypted_text = input()
    if encrypted_text == "find":
        break

    key_index = 0
    for char in encrypted_text:
        decrypted_text += chr(ord(char) - key[key_index])
        key_index = (key_index + 1) % len(key)

    start = decrypted_text.find("&")
    end = decrypted_text.find("&", start + 1)
    treasure_type = decrypted_text[start + 1:end]

    start = decrypted_text.find("<")
    end = decrypted_text.find(">", start + 1)
    value = decrypted_text[start + 1:end]

    print(f"Found {treasure_type} at {value}")
    decrypted_text = ""