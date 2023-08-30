from utils.display_utils import display_admin_menu
from utils.input_utils import take_choice

def admin_entry():
    flag1 = True
    while flag1:
        display_admin_menu()
        admin_choice = take_choice()
        if admin_choice == 1:
            print("BOOKs Menu")
        elif admin_choice == 2:
            print("STUDENTs Menu")
        elif admin_choice == 3:
            print("TEACHERs Menu")
        elif admin_choice == 4:
            flag1 = False
            print("Logout")
        else:
            print("Please enter only 1,2,3,4 only")