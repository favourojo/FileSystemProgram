# Python program to handle directory and files operations in Python

# import modules
import os
import time
from os import scandir
import shutil
import random
import string
import string
import datetime
from datetime import datetime
import sys
import zipfile
from pathlib import Path
import csv 
import random 
from csv import writer
from faker import Faker 

# Path of file
N_PATH = 'C:\\Users\\favou\\Documents\\cs400\\computer-science-400-fall-2022-long-term-systems-project-favourojo\\project\\data\\names.csv'

# Creating a directory
def create_dir():
    """Creates a directory that will include the file"""
    outdir = Path.cwd() / "data"
    if Path.exists(outdir) == True:
        print("Directory already exists!")
    else:
        outdir.mkdir(parents=True, exist_ok=True)
        print("Directory created!")

    return outdir

# Adding files to a directory 
def create_file():
    """Generates fake names to CSV file"""
    # creating Faker module
    fake = Faker()
    fake.name()
    
    # writing into files
    with open(N_PATH, 'a') as csvfile:
        filewriter = csv.writer(csvfile)
        for i in range(10):
            filewriter.writerow([fake.name()])

        myFile = open(N_PATH, "r")
        print(myFile.read())
        myFile.close()

# Getting file attributes
def attributes():
    """Retrieving the file attributes of the specific file"""
    with os.scandir('data') as dir_contents:
        for entry in dir_contents:
            info = entry.stat()
            print(info.st_mtime)

# Time stamp for file
def convert_date(timestamp):
    """Retrieving the time stamp for the specific file"""
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

# Displaying attributes of file
def get_files():
    dir_entries = scandir('data/')
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            stat = os.stat(N_PATH)
            print(f'{entry.name}\t')
            print("\nSize: %s bytes" % stat.st_size)
            print("\nLast accessed: %s" % time.ctime(stat.st_atime))
            print(f'Last Modified: {convert_date(info.st_mtime)}')

# Get the file's permissions
def permission():
    """Displaying the read, write, and execute permissions of the file"""
    file_path = N_PATH
    permissions = os.stat(file_path).st_mode

    # Print the read and write permissions
    print('Read permission:', bool(permissions & 0o400))
    print('Write permission:', bool(permissions & 0o200))
    print('Execute permission:', bool(permissions & 0o100))

# Main function 
if __name__ == '__main__':
    try:
        print("\nWelcome to the File System Program!")
        print("-------------------------------------")
        print("\nContent of the File System Program will be in the", sys.argv[0], "program")
        print("\nFirst, lets create the directory: ")

        create_dir()

        
        print("\nYou have successfully created the directory")

        
        print("\nNow, lets add a file into the directory: ")
        
        #file_size = os.stat(N_PATH).st_size
        #if file_size > 0:
         #   print('There is content inside this file')
        #else:
         #   print('There is no content inside this file')

        print("\nHere are the file contents: ")
        create_file()

        if os.path.exists("data/names.csv"):
            print("You have successfully added the file!")
        else:
            print("Does not exist")
        
        print("\nNow, we are going to display the attributes of the file")
        get_files()

        print("\nYou can display the read, write, and execute permissions of the file!")
        permission()


    except KeyboardInterrupt:
        sys.exit(0)
        