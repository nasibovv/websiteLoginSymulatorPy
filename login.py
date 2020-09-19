from dbActions import read_data_from_db
from database import fetch_db

def login():
    while True:
        username = input("Username: ")
        password = input("Password: ")

        flag = fetch_db(username, password)

        if flag is None:
            break
