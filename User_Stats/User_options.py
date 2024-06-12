from User_Stats.User_measurements import add_user_measurements
from User_Stats.weight_graph import Weight_main
from User_Stats.Calculate_BMI import BMI_calculation

def operation_options():
    printLines()
    print("1. Add User measurements\n2. Draw weight graph \n3. Calculate BMI \n0. Sign out\n")
    user_input = input("Enter Your Option: ")
    return user_input

def printLines():
    print("-" * 100)


def Logged_in_User_options(user_id):
    while True:
        choice = operation_options()    
        if choice == '1':
            add_user_measurements(user_id)
        elif choice == '2':
            Weight_main(user_id)
        elif choice == '3':
            BMI_calculation()
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")