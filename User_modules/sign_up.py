from User_modules.user import User
from User_modules.csv_operations import save_to_csv, load_from_csv

import uuid

#user inputs for sign up
def sign_up_inputs():
    while True:
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        gender = input("Enter gender (Male, Female): ")

        if username != "" and email != "" and password != "" and gender != "":
            return username, email, password, gender
        else:
            print("All Arguments must be filled")
            continue


def sign_up():
    user_exists = False
    username, email, password, gender = sign_up_inputs()    #geting user parameters
    users = load_from_csv("csvFiles/users.csv") # reading csv file
    for user in users:
        if user.get_email() == email:   #check if mail exists
            user_exists = True

    if not user_exists:
        user_id = uuid.uuid4() # generating id for user
        user = User(user_id, username, email, gender, password) # creating object
        save_to_csv(user, "csvFiles/users.csv") # adding to csv
        print("User added successfully")
    else:
        print("User with this email already exists, please enter a different email")
