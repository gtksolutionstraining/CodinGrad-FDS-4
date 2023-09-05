import json

def read_json(file_path):
    with open(file_path,"r") as file:
        LMS = json.load(file)
    return LMS

def write_json(file_path,LMS):
    with open(file_path,"w") as file:
        file.write(str(LMS).replace('\'','"'))

