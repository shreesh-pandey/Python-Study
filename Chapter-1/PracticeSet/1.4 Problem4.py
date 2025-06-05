# Q: Write a python program to print the contents of a directory using the os module. Search online for the function which does that.

# File name: list_dir.py

import os  # Import the os module

# Get current working directory
print("Current Directory:", os.getcwd())

# List all files and folders in the current directory
contents = os.listdir()  

print("Contents of the directory:")
for item in contents:
    print("-", item)

