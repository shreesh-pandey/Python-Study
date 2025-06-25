# You're building a simple password checking tool.
    # You have a list of saved passwords.
    # Ask the user to enter a password.
    # Loop through the list to check if it matches any saved one.
    # If it finds a match, stop checking and print success.
    # If it finds a blank or invalid password in the list, just skip it.
    # If the password isn't found after checking all, print failure using else.
    # Use pass to handle future cases where a password is locked (but take no action for now).

# Lets start with a list of passwords.
passwords = ["admin123", "password123", "abc123", "security123", "administor123", ""]
locked_passwords = []

# There are many ways to write this program but since we are studying for-else, we will use it.
# Lets start with asking the user to input the password.
user_password = input("Please enter your password: ").lower()
# Now lets use for-else to match the input with the list.``
for pwd in passwords:
    if pwd == "":
        continue    # Skip blank passwords
    elif pwd in locked_passwords:
        pass    # Placeholder for locked password handling
    elif pwd == user_password:
        print("Password matched! Access granted!")
        break
else:
    print("Password mismmatch! Access denied!")