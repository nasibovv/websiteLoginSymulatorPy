<<<<<<< HEAD
import json
import time

def authorize_user():

        au_user = input("Enter username of user you want to authorize:")
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


def write_json_user_au(index, au_check):
    def write_json(data, filename="userDB.json"):
        with open(filename, "w") as f:
            json.dump(data, f)

    with open("userDB.json") as user_file:
        data = json.load(user_file)
        temp = data["users"][index]
        print(au_check)
        print(temp)
        user = {"authority": au_check}
        temp.dump(user)

    write_json(data)


def superAdmin():
    while True:
        print("\n******* Super Admin Control page *******")
        print("1. Authorize User")
        print("2. Ban User")
        print("3. Ban User")
        print("4. Edit User Info")
        print("5. Add User")
        print("6. Reset")
        print("7. Exit System")

        choice = int(input("\nEnter Choice: "))

        if choice == 1:
            authorize_user()


def admin():
    pass


def editor():
    pass


def authority_check(index):
    with open("userDB.json") as user_file:
        data = json.load(user_file)

        if data["users"][index]["authority"] == "superAdmin":
            superAdmin()
        elif data["users"][index]["authority"] == "admin":
            admin()
        elif data["users"][index]["authority"] == "editor":
            editor()
        else:
            print("\n******* Welcome to user interface *******")
=======
import json
import time

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


def superAdmin():
    while True:
        print("\n******* Super Admin Control Panel *******")
        print("1. Authorize User")
        print("2. Ban/Unban User")
        print("3. Edit User Info")
        print("4. Add User")
        print("5. Reset")
        print("6. Exit System")

        choice = int(input("\nEnter Choice: "))

        if choice == 1:
            authorize_user()
        elif choice == 2:
            user_status_change()
        elif choice == 3:
            pass
        elif choice == 4:
            admin_add()
        elif choice == 5:
            pass
        elif choice == 6:
            break


def admin():
    pass


def editor():
    pass


def authority_check(index):
    with open("userDB.json") as user_file:
        data = json.load(user_file)

        if data["users"][index]["authority"] == "superAdmin":
            superAdmin()
        elif data["users"][index]["authority"] == "admin":
            admin()
        elif data["users"][index]["authority"] == "editor":
            editor()
        else:
            print("\n******* Welcome to user interface *******")
>>>>>>> bcd75ca... Fourth commit, added new features
