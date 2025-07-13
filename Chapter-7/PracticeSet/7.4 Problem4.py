# Q.4: Write a program to calculate the factorial of a given number using a while loop.

# Ask the user to enter a number
number = int(input("Please enter the number to calculate factorial: "))

# Initialize factorial to 1 (since 1 is the identity for multiplication)
factorial = 1
i = 1

# Use a while loop to multiply all numbers from 1 to 'number'
while i <= number:
    factorial *= i
    i += 1

# Print the result
print(f"The factorial for the number {number} is: {factorial}")
