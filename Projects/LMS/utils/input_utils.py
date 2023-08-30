def take_choice():
    flag  = True
    while flag:
        try:
            choice = int(input("Please enter your choice: "))
            return choice
        except ValueError as ve:
            print("Please enter numbers only!")