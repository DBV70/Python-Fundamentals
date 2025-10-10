def password_validator(password):
    password_length_ok = len(password) in range(6, 10)
    password_characters_ok = True
    password_digits_ok = True
    nr_digits = 0
    for char in password:
        if not char.isalpha() and not char.isdigit():
            password_characters_ok = False
        if char.isdigit():
            nr_digits += 1
    if nr_digits < 2:
        password_digits_ok = False

    if password_length_ok and password_characters_ok and password_digits_ok:
        print("Password is valid")
    if not password_length_ok:
        print("Password must be between 6 and 10 characters")
    if not password_characters_ok:
        print("Password must consist only of letters and digits")
    if not password_digits_ok:
        print("Password must have at least 2 digits")

input_password = input()
password_validator(input_password)
