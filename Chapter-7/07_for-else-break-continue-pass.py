# for-else Statement

# Syntax
# for item in sequence:
#     if condition:
#         break  # loop ends here, else block won't run
# else:
#     # this runs only if the loop wasn't broken

# Example: Searching for a number

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 7:
        print("Found 7!")
        break
else:
    print("7 was not found.")


# Output:
# 7 was not found.


# Explanation:

# - Loop checks each number.
# - 7 isn’t found → loop ends normally → else runs.

# Now try with 7 in the list:


# numbers = [1, 2, 7, 3, 4]

for num in numbers:
    if num == 7:
        print("Found 7!")
        break
else:
    print("7 was not found.")


# Output:
# Found 7!

# Because break was used, the else block did not run.

# -------------------------- -------------------------- -------------------------- #

# break function: Exit the Loop Early

# Example:

for i in range(10):
    if i == 5:
        break
    print(i)


# Output:
# 0
# 1
# 2
# 3
# 4

# When i is 5, break stops the loop.

# -------------------------- -------------------------- -------------------------- #

# 2. continue : Skip the Current Iteration

# Example:

for i in range(5):
    if i == 2:
        continue
    print(i)


# Output:
# 0
# 1
# 3
# 4


# When i is 2, it skips printing and goes to the next number.

# -------------------------- -------------------------- -------------------------- #

# 3. pass : Do Nothing (Placeholder)

# Example:

for i in range(3):
    pass  # we'll add code here later

print("Loop finished")


# Output:
# Loop finished

# Pass just fills the space. It doesn’t affect the loop at all.

# -------------------------- -------------------------- -------------------------- #

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