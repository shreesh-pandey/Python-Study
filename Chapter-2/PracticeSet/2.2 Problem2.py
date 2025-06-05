# Q.2: Find the remainder when a number is divided by another.

# Lets take two variable a & b.
# Lets use input() fuction to ask numbers from the user.

a = input("Input the Divident: ")
b = input("Input the Divider: ")

# Since input() fuction considers all inputs as "Strings", lets use int() function to convert strings to Integers

# Last time we converted variables into the integers in the calculation code itself.
# Reminder = int(a)% int(b)

# This time, lets change them first and then do the calculation.
a = int(a)
b = int(b)

Remainder = a % b # We will use % (Modulus) operator to find the remainder.

print("The reminder is:", Remainder) # Ex: If a = 3, & b = 2, the Output will be => The reminder is: 1.