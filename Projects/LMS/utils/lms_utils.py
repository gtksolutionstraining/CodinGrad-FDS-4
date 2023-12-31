from utils.input_utils import (
    take_choice,
    take_user_password
)
from utils.display_utils import (
    display_main_menu
)
from utils.admin_utils import admin_entry
from utils.file_utils import write_json
from config import(
    CONFIG_JSON_PATH,
    LMS
)
def lms_entry():
    flag = True
    while flag:
        display_main_menu()
        choice = take_choice()
        if choice == 1:
            login_status = take_user_password()
            if login_status:
                admin_entry()
            else:
                print("Wrong Credentials!")
        elif choice == 2:
            print("THIS IS STUDENT MENU")
        elif choice == 3:
            print("THIS IS TEACHER MENU")
        elif choice == 4:
            flag = False
            write_json(CONFIG_JSON_PATH,LMS)
            print("Thank you for using I am shutting down")
        else:
            print("Wrong input, please select 1,2,3,4 only.")