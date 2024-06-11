from user import User


def operation_options():
    printLines()
    print("1. Login\n2. Sign Up\n0. Exit\n")
    user_input = input("Enter Your Option: ")
    return user_input


def printLines():
    print("-" * 100)


def authentication():
    while True:
        user_Input = operation_options()
        if user_Input == '1':
            login = User.login()
            if login == True:
                break
            else:
                continue

        elif user_Input == '2':
            User.sign_up()

        elif user_Input == '0':
            print('Exit')
            break

        else:
            printLines()
            print("Invalid input")