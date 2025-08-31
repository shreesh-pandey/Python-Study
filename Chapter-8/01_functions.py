# Lets write a program that uses a function to prints the multiplication of two numbers.

def multiply(x, y):
    """Returns the product of two numbers."""
    result = x * y
    return result

# Function Call

product = multiply(4, 5)
print(product)  # Output: 20

# -------------------------- -------------------------- -------------------------- #

# We can also make it better by allowing users to input numbers

def product():
    a = int(input("Please input the first no.: "))
    b = int(input("Please input the second no.: "))
              
    """Returns the product of two numbers.""" 
    result = a * b
    return result

# Function Call

answer = product()
print(answer)