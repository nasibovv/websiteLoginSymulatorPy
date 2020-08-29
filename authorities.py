import json


def superAdmin():
    pass


def admin():
    pass


def editor():
    pass


def authority_check():
    with open("userDB.json") as user_file:
        data = json.load(user_file)

    for user_authority in data["users"]:
        if user_authority["authority"] == "superAdmin":
            superAdmin()
        elif user_authority["authority"] == "admin":
            admin()
        elif user_authority["authority"] == "editor":
            editor()
        else:
            print("Welcome to user interface")