
class User_parameters:
    #constuctor
    def __init__(self, user_id, age, height, weight, date):

        self.user_id = user_id
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
    
    def get_id(self):
        return self.user_id