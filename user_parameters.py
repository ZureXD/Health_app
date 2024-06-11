import csv
import os
import datetime


class User_parameters:
    #constuctor
    def __init__(self, username, gender, age, height, weight, date):

        self.username = username
        self.gender = gender
        self.age = age
        self.height = height
        self.weight = weight
        self.time = date   
        

    #Set user parameters
    def set_age(self):
        self.age = input("Enter your age: ")

    def set_heigh(self):
        self.height = input("Enter your height: ")

    def set_weight(self):
        self.weight = input("Enter your weight: ")


    #Get user parameters
    def get_age(self):
        return self.age

    def get_height(self):
        return self.height
    
    def get_weight(self):
        return self.weight
    

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

    '''def BMI_calculator(age,height,weight):
        if age < 20:
            print("lol")
        elif age >= 20:
            BMI = weight/(height*height)

        '''

'''user1 = User_parameters("salo","Female",26,175,63,datetime.date.today())
user1.save_to_csv_all_users("csvFiles/AlluserStatistics.csv")
user1 = Indiviadual_parameters(26,175,63,datetime.date.today())
user1.load_from_csv_individual("csvFiles/Individual_csvFiles/" + "zura" + ".csv")
user1.save_to_csv_individual("csvFiles/Individual_csvFiles/" + "zura" + ".csv")'''

def main():
    print("hello")