import json


def name_validation():
    while True:
        name = input("\nYour Name: ")
        check = any(char.isdigit() for char in name)

        if check:
            print("Invalid input! Try again!")
        else:
            break
    return name.title()


def surname_validation():
    while True:
        surname = input("\nYour Surname: ")
        check = any(char.isdigit() for char in surname)

        if check:
            print("Invalid input! Try again!")
        else:
            break
    return surname.title()


def username_validation():
    username = input("\nYour Username: ")

    with open("userDB.json") as user_file:
        data = json.load(user_file)

        for user_name in data["users"]:
            if user_name["username"] == username:
                while True:
                    print("Invalid input! Username has already taken. Try again!")
                    username = input("\nYour Username: ")
                    if user_name["username"]:
                        break
    return username


def password_validation():
    while True:
        password = input("\nYour Password: ")

        if len(password) > 16 or len(password) < 8:
            print("Password should include min 8, max 16 characters! Try again!")

        if not password.isdigit or password.isdigit():
            print("Password should include both numbers and letters! Try again!")

        else:
            break

    while True:
        password2 = input("Reenter Your Password: ")

        if password != password2:
            print("Passwords are not same! Try again!")

        else:
            break

    return password
