import json
import time
import sqlite3
from register import registerUser


def authorize_user():
    au_user = input("Enter username of user you want to authorize: ")
    au_check = input("As 'editor' or 'admin': ")

    with open("userDB.json") as user_file:
        data = json.load(user_file)

    for user_username in data["users"]:
        if user_username["username"] == au_user:

            if au_check == "editor":
                user_username["authority"] = au_check

                with open("userDB.json", "w") as user_file:
                    json.dump(data, user_file)

                print("\nUser has successfully authorized\nRedirecting to Control Panel...")
                time.sleep(3)

            elif au_check == "admin":
                user_username["authority"] = au_check

                with open("userDB.json", "w") as user_file:
                    json.dump(data, user_file)

                print("\nUser has successfully authorized\nRedirecting to Control Panel...")
                time.sleep(3)

            else:
                print("Invalid Input")


def user_status_change():
    user_ban = input("Input username you want to ban/unban: ")

    with open("userDB.json") as user_file:
        data = json.load(user_file)

    for user_username in data["users"]:
        if user_username["username"] == user_ban:

            if user_username["status"] == "active":
                user_username["status"] = "banned"

                with open("userDB.json", "w") as user_file:
                    json.dump(data, user_file)

                print("\nUser status has successfully changed!\nRedirecting to Control Panel...")
                time.sleep(3)

            elif user_username["status"] == "banned":
                user_username["status"] = "active"

                with open("userDB.json", "w") as user_file:
                    json.dump(data, user_file)

                print("\nUser status has successfully changed!\nRedirecting to Control Panel...")
                time.sleep(3)
            else:
                print("Invalid Input!")


def admin_add():
    def write_json(data, filename="userDB.json"):
        with open(filename, "w") as f:
            json.dump(data, f)

    registeredUser = registerUser()

    with open("userDB.json") as user_file:
        data = json.load(user_file)
        temp = data["users"]
        user = {"user_id": registeredUser.user_id, "name": registeredUser.name, "surname": registeredUser.surname,
                "username": registeredUser.username, "password": registeredUser.password,
                "authority": registeredUser.authority, "status": registeredUser.status}
        temp.append(user)

    write_json(data)


def pass_reset():
    user_pass_reset = input("Input username for pass reset: ")

    with open("userDB.json") as user_file:
        data = json.load(user_file)

    for user_username in data["users"]:
        if user_username["username"] == user_pass_reset:
            user_username["password"] = "default12345"

            with open("userDB.json", "w") as user_file:
                json.dump(data, user_file)

            print("\nUser password has successfully has been reset!\nRedirecting to Control Panel...")
            time.sleep(3)
    else:
        print("Invalid Input!")


def superAdmin():
    while True:
        print("\n******* Super Admin Control Panel *******")
        print("1. Authorize User")
        print("2. Ban/Unban User")
        print("3. Add User")
        print("4. Reset")
        print("5. Exit System")

        choice = int(input("\nEnter Choice: "))

        if choice == 1:
            authorize_user()
        elif choice == 2:
            user_status_change()
        elif choice == 3:
            admin_add()
        elif choice == 4:
            pass_reset()
        elif choice == 5:
            break


def admin():
    while True:
        print("\n******* Admin Control Panel *******")
        print("1. Ban/Unban User")
        print("2. Add User")
        print("3. Exit System")

        choice = int(input("\nEnter Choice: "))

        if choice == 1:
            user_status_change()
        elif choice == 2:
            admin_add()
        elif choice == 3:
            break


def editor():
    while True:
        print("\n******* Editor Control Panel *******")
        print("1. Add User")
        print("2. Publish article")
        print("3. Exit System")

        choice = int(input("\nEnter Choice: "))

        if choice == 1:
            admin_add()
        elif choice == 2:
            print("\nThis feature is for real-life projects")
            time.sleep(3)
        elif choice == 3:
            break


def authority_check(login_username):

    con = sqlite3.connect("user.db")

    cursor = con.cursor()
    current = cursor.execute("SELECT Status FROM Users")
        
    if current == "superAdmin":
        superAdmin()
    elif current == "admin":
        admin()
    elif current == "editor":
        editor()
    else:
        print("\n******* Welcome to user interface *******\n")
