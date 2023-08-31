from config import LMS
from utils.display_utils import display_depts_menu
def take_choice():
    flag  = True
    while flag:
        try:
            choice = int(input("Please enter your choice: "))
            return choice
        except ValueError as ve:
            print("Please enter numbers only!")

## Give user 2 more chances if user gives correct username but wrong password
def take_user_password():
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")
    for admin in LMS['Admins']:
        if user_name == admin['USER'] \
        and password == admin['PASSWORD']:
            print("Login Successfull!")
            return True
    return False

#Show a menu of depts to user
def take_dept():
    display_depts_menu()
    flag = True
    while flag:
        choice = take_choice()
        if choice < 3 and choice > 0:
            flag = False
        else:
            print("Please enter 1,2 only")
    return choice

def take_year():
    flag  = True
    while flag:
        try:
            year = int(input("Enter your year: "))
            if year < 5 and year > 0:
                return year
            else:
                print("Please enter 1,2,3,4 only!")
        except ValueError as ve:
            print("Please enter 1,2,3,4 only!")

def take_sem():
    flag  = True
    while flag:
        try:
            sem = int(input("Enter your sem: "))
            if sem < 3 and sem > 0:
                return sem
            else:
                print("Please enter 1,2 only!")
        except ValueError as ve:
            print("Please enter 1,2 only!")

def take_book_details():
    book_name = input("Enter book name: ")
    book_id = input("Enter book id: ")
    return book_name,book_id