import csv
import os
from User_modules.user import User

def save_to_csv(user, csvpath):
    with open(csvpath, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user.username, user.email, user.gender, user.get_password()])

def load_from_csv(csvpath):
    users = []
    if os.path.exists(csvpath):
        with open(csvpath, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                users.append(User(username=row[0], email=row[1], gender=row[2], hash_password=row[3]))
    return users