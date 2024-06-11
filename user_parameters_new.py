from user_parameters import User_parameters

import csv
import os
import datetime

user = User_parameters()

#CSV file manipulations        
def save_to_csv_all_users(self, csvpath):
    with open(csvpath, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([self.username, self.gender, self.age, self.height, self.weight])

@staticmethod
def load_from_csv_all_users(csvpath):
    users = []
    if os.path.exists(csvpath):
        with open(csvpath, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                users.append(User_parameters(username=row[0],gender=row[1],age=row[2],height=row[3],weight=row[4]))
    return users


class Indiviadual_parameters(User_parameters):
#constructor
def __init__(self, age, height, weight, date):
    super().__init__(username=None, gender=None, age=age, height=height, weight=weight, date=date)
    

def save_to_csv_individual(self, csvpath):
    with open(csvpath, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([self.age, self.height, self.weight, self.time])


@staticmethod
def load_from_csv_individual(csvpath):
    users = []
    if os.path.exists(csvpath):
        with open(csvpath, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                users.append(Indiviadual_parameters(age=row[0],height=row[1],weight=row[2],date=row[3]))
    return users