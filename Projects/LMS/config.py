# It holds all the configuration and global variables, constants required by the software
"""
Data Schema
Skeleton Database
"""
from utils.file_utils import read_json

CONFIG_JSON_PATH = "assets/config.json"
LMS = read_json(CONFIG_JSON_PATH)

# LMS = {}
# LMS['Admins'] = [
#     {
#         "USER":"CodinGrad",
#         "PASSWORD":"CodinGrad"
#     }
# ]
# LMS['Books'] = {}
# LMS['Books']['CSE'] = {}
# LMS['Books']['CSE']['1stYr'] = {}
# LMS['Books']['CSE']['1stYr']['1stSem'] = [] #List of Books of CSE,1styr,1stsem
# LMS['Students'] = {}
# LMS['Students']['CSE'] = {}
# LMS['Students']['CSE']['1stYr'] = {}
# LMS['Students']['CSE']['1stYr']['1stSem'] = [] #List of students of CSE,1styr,1stsem
# LMS['Teachers'] = {}
# LMS['Teachers']['CSE'] = [] #List of Teachers in dept

#mappers
yr_map = {
    1:"1stYr",
    2:"2ndYr",
    3:"3rdYr",
    4:"4thYr"
}

sem_map ={
    1:"1stSem",
    2:"2ndSem"
}

dept_map = {
    1:"CSE",
    2:"CIVIL"
}