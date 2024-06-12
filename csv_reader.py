import csv

def load_data(filename):
    mylist = []
    '''with open(filename, mode='r', newline='') as Users:
        Users_data = csv.reader(Users, delimiter=',')
        for row in Users_data:
            mylist.append(row)'''
    with open(filename, mode='r', newline='') as Users:
        Users_data = csv.reader(Users,delimiter='\n')
        for row in Users_data:
            # Extract the last element from each row (the date)
            mylist.append(row[-1])
    return mylist  
