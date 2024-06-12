import csv
import os
from User_modules.user import User

def save_to_csv(user, csvpath):
    with open(csvpath, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([user.user_id ,user.username, user.email, user.gender, user.get_password()])

def load_from_csv(csvpath):
    users = []
    if os.path.exists(csvpath):
        with open(csvpath, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                users.append(User(user_id=row[0],username=row[1], email=row[2], gender=row[3], hash_password=row[4]))
    return users