# Q.5: Write a Python program to check whether a username is valid or not. The username is considered valid only if:
        # 1. It contains less than 10 characters, and
        # 2. It is not already taken (i.e. not present in the list of existing usernames)
# You also have to display whether the username is valid or invalid, along with the reason.

# Lets start with creating a list of names that will act as usernames.
usernames = ["shreesh", "pritha", "rubai"]

# That been set, lets ask user to enter their name that will act as their username.
name = input("Please enter your name that will be your username: ").lower()

# Now lets check the validity of the username by validating the conditions.
if len(name)>10:
    print("Try again! The length of username is greater than 10")
elif name in usernames:
    print("Try again! The username is already taken")
else:
    print("Congratulations! Username is valid and available!")