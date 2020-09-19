from database import add_db
from login import login

while True:
    print("\n******* Welcome! *******\n")
    print("1. Sign in")
    print("2. Sign up")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_db()
    elif choice == "2":
        login()
    elif choice == "3":
        exit()
