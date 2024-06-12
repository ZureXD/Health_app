from User_modules.csv_operations import load_from_csv

def login_inputs():
    username_email = input("Enter email: ")
    password = input("Enter password: ")
    return username_email, password

def login_user():
    login_status = False
    user_id = ""
    email, password = login_inputs()
    users = load_from_csv("csvFiles/users.csv")
    for user in users:
        if user.get_email() == email:
            if user.check_password(password, user.get_password()):
                print("Login successful")
                login_status = True
                user_id = user.get_user_id()
                return login_status,user_id
            else:
                print("Incorrect password")
                login_status = False
                return login_status,user_id
    print("User not found")
    return login_status,user_id