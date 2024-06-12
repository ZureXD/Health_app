from User_Stats.user_parameters import User_parameters
from User_Stats.csv_operations import save_to_csv_all_users
import datetime

def user_measurements():
    while True:
        try:
            age = int(input("Enter age: "))
            height = float(input("Enter height: "))
            weight = float(input("Enter weight: "))
            break
        except ValueError:
            print("Invalid inputs, please enter valid arguments")
    return age, height, weight

def add_user_measurements(user_id):
    date = datetime.date.today()
    age,height,weight = user_measurements()    
    #users = load_from_csv("csvFiles/AlluserStatistics.csv")
    
    user = User_parameters(user_id,age,height,weight,date)
    save_to_csv_all_users(user, "csvFiles/AlluserStatistics.csv")
    print("User parameters added")