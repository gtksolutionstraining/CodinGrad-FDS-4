from utils.input_utils import(
    take_dept,
    take_year,
    take_sem
)
from config import (
    LMS,
    yr_map,
    sem_map,
    dept_map
)
def get_details():
    dept = take_dept()
    dept = dept_map[dept]
    year = take_year()
    year = yr_map[year]
    sem = take_sem()
    sem = sem_map[sem]
    return dept,year,sem

def add_book(book_name,book_id):
    dept,year,sem = get_details()
    book = {
        "Name":book_name,
        "Id":book_id
    }
    LMS['Books'][dept][year][sem].append(book)
    print("Book added successfully!")

def get_all_books():
    dept,year,sem = get_details()
    print(LMS['Books'][dept][year][sem])