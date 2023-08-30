from utils.input_utils import take_choice
from utils.display_utils import (
    display_main_menu
)
from utils.admin_utils import admin_entry
def lms_entry():
    flag = True
    while flag:
        display_main_menu()
        choice = take_choice()
        if choice == 1:
            admin_entry()
        elif choice == 2:
            print("THIS IS STUDENT MENU")
        elif choice == 3:
            print("THIS IS TEACHER MENU")
        elif choice == 4:
            flag = False
            print("Thank you for using I am shutting down")
        else:
            print("Wrong input, please select 1,2,3,4 only.")