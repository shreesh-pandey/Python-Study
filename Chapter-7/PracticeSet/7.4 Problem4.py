# Q.4: Write a program to calculate the factorial of a given number using a while loop.

# -------------------------- -------------------------- -------------------------- #

# Solution:

# Lets start with asking the user to enter the number.
number = int(input("Please enter the number to calculate factorial: "))

# Now lets use while loop to calculate the factorial for the given number

factorial = 0
i = 1
while (i <= number):
    factorial = i*(i+1)
    i+=1

print(f"The factorial for the number {number} is: {factorial}")