from User_modules.authorization import authentication
from User_Stats.User_options import Logged_in_User_options

while True: 

    current_user = authentication()

    Logged_in_User_options(current_user)