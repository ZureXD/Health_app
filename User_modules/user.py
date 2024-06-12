import hashlib
import uuid

class User:
    def __init__(self, user_id, username, email, gender, password=None, hash_password=None):

        self.user_id = user_id
        self.username = username
        self.email = email
        self.gender = gender
        self.__password = ""
        
        #checks which password type is given
        if password is not None:
            self.__password = self.__hash_password(password)    # Hashing the password
        elif hash_password is not None:
            self.__password = hash_password
        else:
            print("Invalid argument")

    #setters
    def set_user_id(self):
        self.user_id = uuid.uuid4()

    def set_username(self, new_username: str):
        self.username = new_username

    def set_email(self, new_email: str):
        self.email = new_email

    def set_password(self, __new_password):
        self.__password = __new_password

    #getters
    def get_user_id(self):
        return self.user_id
    
    def get_username(self):
        return self.username

    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.__password
    
    def get_gender(self):
        return self.gender

    #password manipulation
    def __hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password, hashed_password):
        if hashed_password == self.__hash_password(password):
            return True
        return False


'''import hashlib


class User:
    #constuctor
    def __init__(self, username, email, gender, password = None, hash_password = None):

        self.username = username
        self.email = email
        self.gender = gender
        self.__password = ""

        #checks which password type is given
        if password is not None:
            self.__password = self.__hash_password(password)    # Hashing the password
        elif hash_password is not None:
            self.__password = hash_password     
        else:
            print("Invalid argument blalba")
        
        

    #Set user parameters
    def set_username(self):
        self.username = input("Enter username: ")

    def set_email(self):
        self.email = input("Enter email address: ")

    def set_password(self):
        self.__password = input("Enter password: ")


    #Get user parameters
    def get_username(self):
        return self.username

    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.__password
    
    def get_gender(self):
        return self.gender
    

    #CSV file manipulations        
    def save_to_csv(self, csvpath):
        with open(csvpath, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.username, self.email, self.gender, self.__password])
    
    def __hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    

    @staticmethod
    def load_from_csv(csvpath):
        users = []
        if os.path.exists(csvpath):
            with open(csvpath, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    users.append(User(username=row[0],email=row[1],gender=row[2],hash_password=row[3]))
        return users
    


    #login functions
    @staticmethod
    def login_inputs():
        username_email = input("Enter usename/email: ")
        password = input("Enter password: ")
        return username_email,password


    def check_password(self, password, hashed_password):
        # Hash the provided password and compare it with the stored hashed password        
        if hashed_password == self.__hash_password(password):
            return True
        else:
            return False
          
    @staticmethod
    def login():
        login_status = False
        username_email,password = User.login_inputs()
        users = User.load_from_csv("csvFiles/users.csv")
        for user in users:
            if user.get_email() == username_email or user.get_username() == username_email:
                if user.check_password(password,user.get_password()):
                    print("Login successful")
                    login_status = True
                    return login_status
                else:
                    print("Incorrect password")
                    login_status = False
                    return login_status
        print("User not found")


    #Sign_up
    @staticmethod
    def sign_up_inputs():
        username = input("Enter usename: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        gender = input("Enter gender (Male,Female): ")
        return username,email,password,gender

    @staticmethod
    def sign_up():
        user_exists = False
        username,email,password,gender = User.sign_up_inputs()
        users = User.load_from_csv("csvFiles/users.csv")
        for user in users:
            if user.get_email() == email or user.get_username() == username:
                user_exists = True

        if user_exists == False:
            user = User(username,email,gender,password)    #creates a user
            user.save_to_csv("csvFiles/users.csv")
            print("User added successfully")
        else:
            print("User already exists, please enter different username/email")'''