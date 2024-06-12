import csv
import os

from User_Stats.user_parameters import User_parameters


#CSV file manipulations        
def save_to_csv_all_users(self, csvpath):
    with open(csvpath, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([self.user_id, self.age, self.height, self.weight, self.time])

@staticmethod
def load_from_csv_all_users(csvpath):
    users = []
    if os.path.exists(csvpath):
        with open(csvpath, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                users.append(User_parameters(user_id=row[0],gender=row[1],age=row[2],height=row[3],weight=row[4],date=row[5]))
    return users