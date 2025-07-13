# Q.5: Write a program to calculate the factorial of a given number using a for loop. Also, handle error cases like negative numbers.

# Ask the user to enter a number
number = int(input("Please enter the number to calculate factorial: "))

# Check if the number is less than 0
if number < 0:
    print("Factorial is not defined for negative numbers. Please enter a non-negative number.")
else:
    # Initialize factorial to 1 (0! = 1 by definition)
    factorial = 1

    # Multiply all numbers from 1 to 'number' to calculate factorial
    for i in range(1, number + 1):
        factorial *= i

    # Print the result
    print(f"The factorial of {number} is: {factorial}")

