# Q.2: Write a program that greets only the people whose names contains a specific letter.
    # Ask the user for a list of names (comma-separated).
    # Ask the user for a letter to check.
    # Greet only the names that start with that letter (case-insensitive).
    # Example greeting: "Hello, Soham!"

# -------------------------- -------------------------- -------------------------- #

# Solution:

# Ask the user to enter names separated by commas
input_names = input("Please enter the names separated by commas: ")
names = input_names.split(",")  # Create a list 'names' from the input string

# Ask the user to input the letter to search for
letter = input("Please enter the letter you want to search for in the names: ").lower()

found = False
for name in names:
    # Check if the letter exists anywhere in the name
    # If you only want names that start with the letter, use: name.strip().lower().startswith(letter)
    if letter in name.strip().lower():
        print(f"Hello! {name.strip().title()}")  # .strip() removes extra spaces, .title() capitalizes nicely
        found = True

# If no name contained the letter
if not found:  # 'not' flips the value of found; so True becomes False and vice versa
    print(f"Sorry, there are no names in the list with the letter '{letter.capitalize()}'.")

