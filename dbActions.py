import json
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
                "username": registeredUser.username, "password": registeredUser.password}
        temp.append(user)

    write_json(data)
