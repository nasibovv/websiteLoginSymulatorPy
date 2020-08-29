import random
import json
import time
from registrationValidation import*


class User:
    def __init__(self, name, surname, username, password, user_id, authority):
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        self.user_id = user_id
        self.authority = authority


def id_creator():
    generated_id = random.randint(1000, 9999)

    with open("userDB.json") as user_file:
        data = json.load(user_file)

        for user_id in data["users"]:
            if user_id["user_id"] == generated_id:
                while True:
                    generated_id = random.randint(1000, 9999)
                    if user_id["user_id"] != generated_id:
                        break
    return generated_id


def registerUser():
    userId = id_creator()
    name = name_validation()
    surname = surname_validation()
    username = username_validation()
    password = password_validation()
    authority = "user"

    user = User(name, surname, username, password, userId, authority)
    print("\nRegistration process has successfully finished!")
    print("Redirecting to main menu...\n\n")
    time.sleep(3)

    return user

