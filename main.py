from dbActions import write_json_from_main
from login import login

while True:
    print("\n******* Welcome! *******\n")
    print("1. Sign in")
    print("2. Sign up")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        write_json_from_main()
    elif choice == "2":
        login()
    elif choice == "3":
        exit()
