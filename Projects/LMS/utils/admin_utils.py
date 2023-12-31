from utils.display_utils import (
    display_admin_menu,
    display_books_menu
)
from utils.input_utils import (
    take_choice,
    take_book_details
)
from utils.book_utils import (
    add_book,
    get_all_books
)
def admin_entry():
    flag1 = True
    while flag1:
        display_admin_menu()
        admin_choice = take_choice()
        if admin_choice == 1:
            display_books_menu()
            book_choice = take_choice()
            if book_choice == 1:
                book_name,book_id = take_book_details()
                add_book(book_name,book_id)
            elif book_choice == 2:
                get_all_books()
        elif admin_choice == 2:
            print("STUDENTs Menu")
        elif admin_choice == 3:
            print("TEACHERs Menu")
        elif admin_choice == 4:
            flag1 = False
            print("Logout")
        else:
            print("Please enter only 1,2,3,4 only")