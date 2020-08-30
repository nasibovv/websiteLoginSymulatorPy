from dbActions import read_data_from_db


def login():
    while True:
        username = input("Username: ")
        password = input("Password: ")

        flag = read_data_from_db(username, password)

        if flag is None:
            break
