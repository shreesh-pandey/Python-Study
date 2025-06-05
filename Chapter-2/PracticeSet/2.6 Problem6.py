# Q.6: Write a python program to calculate the square of a number entered by the user.

# Lets as the user to enter the number.
a = input("Enater the number")

# Change the input to integer.
a = int(a)

# Now lets calculate the square root of the number.

SR = a*a

# Print the square root

print("The square root of the number is: ", SR)

# Another way is to use the arithmatic operation: **

SR = a**2

print("The square root of the number is: ", SR)

# ** can be used to calculate the cube of the number and all as well.

CR = a**3
print("The cube of the number is: ", CR)