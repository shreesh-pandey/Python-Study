# Print the multiplication table of a given number from 1 to 10 using a for loop, and then print it in reverse order (from 10 to 1).

# Lets start with asking the user for the number.
number = int(input("Please enter the number for multiplication table: "))

# Lets make it interactive by asking user if they want print the table normally or in reverse.
order = input("Do you want to print the table in reverse? (Y/N): ").lower()

# Now, lets print the table.
print(f"\nThe multiplication table for {number} is:\n")

if order == "y":
    for i in range (10, 0, -1):
        print(f"{number} * {i} = {number * i}")
else:
    for i in range (1, 11):
        print(f"{number} * {i} = {number * i}")



