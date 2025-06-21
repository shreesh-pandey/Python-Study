# Q.2: Rewrite the program in 6.1 with the help of 'list' and 'for' loop.

# First, lets create an empty list.
numbers = []

# Lets start with asking user to input the four numbers.
for i in range(1,5):        # Using the range(1,5) like this so that we can use {i} with fprint while asking to input the numbers.
    num = int(input(f"Enter the number {i}: "))
    numbers.append(num)

# Lets create a variable 'greatest' to store the gratest number of the four.
greatest = numbers[0]       # Assuming that the first number in the list (the number at index 0) is the greatest.
for n in numbers:           # It means: Go through each number (n) in the list numbers, one by one.
    if n > greatest:        # It asks: Is this number (n) bigger than the current greatest?
        greatest = n        # If the above statement is 'Yes', it updates the value of greatest.

print("The greatest number is:", greatest)  # For inputs: [1,2,3,4], the Output: The greatest number is: 4