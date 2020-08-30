<<<<<<< HEAD
import json

from authorities import authority_check
from register import registerUser


def write_json_from_main():
    def write_json(data, filename="userDB.json"):
        with open(filename, "w") as f:
            json.dump(data, f)

    registeredUser = registerUser()

    with open("userDB.json") as user_file:
        data = json.load(user_file)
        temp = data["users"]
        user = {"user_id": registeredUser.user_id, "name": registeredUser.name, "surname": registeredUser.surname,
                "username": registeredUser.username, "password": registeredUser.password,
                "authority": registeredUser.authority}
        temp.append(user)

    write_json(data)


def read_data_from_db(login_username, login_password):
    flag = False

    with open("userDB.json") as user_file:
        data = json.load(user_file)

    if not flag:
        for user_username in data["users"]:
            if user_username["username"] == login_username:
                flag = True
                index = data["users"].index(user_username)

    if not flag:
        print("\nUsername or Password is not correct! Try again! \n")
        return False

    if flag:

        if data["users"][index]["password"] == login_password:
            authority_check(index)
        else:
            print("\nUsername or Password is not correct! Try again!\n")
            return False
=======
import json

from authorities import authority_check
from register import registerUser


def write_json_from_main():
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


def read_data_from_db(login_username, login_password):
    flag = False

    with open("userDB.json") as user_file:
        data = json.load(user_file)

    if not flag:
        for user_username in data["users"]:
            if user_username["username"] == login_username:
                flag = True
                index = data["users"].index(user_username)

    if not flag:
        print("\nUsername or Password is not correct! Try again! \n")
        return False

    if flag:

        if data["users"][index]["password"] == login_password:
            authority_check(index)
        else:
            print("\nUsername or Password is not correct! Try again!\n")
            return False
>>>>>>> bcd75ca... Fourth commit, added new features
