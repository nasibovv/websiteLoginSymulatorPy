import sqlite3
from authorities import authority_check
from register import registerUser
import time

con = sqlite3.connect("user.db")

cursor = con.cursor()

def add_db():
    
    registeredUser = registerUser()

    script = "INSERT INTO Users (User_ID, Name, Surname, Username, Password, Authority, Status) VALUES(?, ?, ?, ?, ?, ?, ?)"

    cursor.execute(script, (registeredUser.user_id, registeredUser.name, registeredUser.surname, registeredUser.username, registeredUser.password, registeredUser.authority, registeredUser.status))
    con.commit()
    con.close()
    

def fetch_db(login_username, login_pass):
    
    flag = False

    if not flag:
        for row in cursor.execute("SELECT Username FROM Users WHERE Username = ?", [login_username]):
            temp = row[0]
            break

        if temp == login_username:
            flag = True

    if not flag:
        print("\nUsername or Password is not correct! Try again! \n")
        return False

    if flag:
        current = cursor.execute("SELECT Status FROM Users")
        
        if current == "banned":
            print("Sorry, your account banned. For more info contact with superadmin@gmail.com")
            time.sleep(2)

        else:
            for row2 in cursor.execute("SELECT Password FROM Users WHERE Password = ?", [login_pass]):
                temp2 = row2[0]
                break
            if temp2 == login_pass:
                authority_check(login_username)
            else:
                print("\nUsername or Password is not correct! Try again!\n")
                return False

