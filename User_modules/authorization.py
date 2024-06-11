from User_modules.sign_up import sign_up
from User_modules.login import login_user


def operation_options():
    printLines()
    print("1. Sign Up\n2. Login\n0. Exit\n")
    user_input = input("Enter Your Option: ")
    return user_input

def printLines():
    print("-" * 100)


def authentication():
    while True:
        choice = operation_options()
    
        if choice == '1':
            sign_up()
        elif choice == '2':
            login, current_user = login_user()
            if login == True:
                break
            else:
                continue
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    return current_user