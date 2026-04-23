#  write a python program to print to content of a directory using the os module
import os

# specify the directory path
directory_path = input("Enter directory path: ")

# check if directory exists
if os.path.exists(directory_path):
    print("\nContents of directory:\n")
    
    for item in os.listdir(directory_path):
        print(item)
else:
    print("Directory does not exist.")