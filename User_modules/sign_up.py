from User_modules.user import User
from User_modules.csv_operations import save_to_csv, load_from_csv

def sign_up_inputs():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    gender = input("Enter gender (Male, Female): ")
    return username, email, password, gender

def sign_up():
    user_exists = False
    username, email, password, gender = sign_up_inputs()
    users = load_from_csv("csvFiles/users.csv")
    for user in users:
        if user.get_email() == email or user.get_username() == username:
            user_exists = True

    if not user_exists:
        user = User(username, email, gender, password)
        save_to_csv(user, "csvFiles/users.csv")
        print("User added successfully")
    else:
        print("User already exists, please enter a different username/email")
