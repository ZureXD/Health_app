from User_modules.csv_operations import load_from_csv

def login_inputs():
    username_email = input("Enter username/email: ")
    password = input("Enter password: ")
    return username_email, password

def login_user():
    login_status = False
    login_username = ""
    username_email, password = login_inputs()
    users = load_from_csv("csvFiles/users.csv")
    for user in users:
        if user.get_email() == username_email or user.get_username() == username_email:
            if user.check_password(password, user.get_password()):
                print("Login successful")
                login_status = True
                login_username = user.get_username()
                return login_status,login_username
            else:
                print("Incorrect password")
                login_status = False
                return login_status,login_username
    print("User not found")
    return login_status,login_username