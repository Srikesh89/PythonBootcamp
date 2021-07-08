import zipfile
import os
import re

#Part 1: Unzip file
# file_to_unzip = 'C://Repos//Udemy_Python_Bootcamp//Jupyter Notebooks//12-Advanced Python Modules//08-Advanced-Python-Module-Exercise//unzip_me_for_instructions.zip'
# unzipped_dir = zipfile.ZipFile(file_to_unzip, 'r')
# unzipped_dir.extractall('C://Repos//Udemy_Python_Bootcamp//Jupyter Notebooks//12-Advanced Python Modules//08-Advanced-Python-Module-Exercise//puzzle')
# unzipped_dir.close()

#Part 2: Traverse directories to find a single phone number
path_to_traverse = 'C://Repos//Udemy_Python_Bootcamp//Jupyter Notebooks//12-Advanced Python Modules//08-Advanced-Python-Module-Exercise//puzzle//extracted_content'
phone_numbers = []

def find_number(file, phone_numbers):
    obj = open(folder+'//'+file, 'r')
    text = obj.read()
    phone_numbers.extend(re.findall(pattern, text))
    obj.close()

for folder, subfolder, file in os.walk(path_to_traverse):
    pattern = r"\d{3}-\d{3}-\d{4}"
    for f in file:
        find_number(f, phone_numbers)
for n in phone_numbers:
    print(n)