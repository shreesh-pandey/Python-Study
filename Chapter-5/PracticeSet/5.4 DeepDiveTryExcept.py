# DEEP DIVE
# In python, we have a functionality to wrap the error part in a 'try-except' to let the program run to completion.
# This way, we can see the error message clearly and the program won’t stop abruptly.
# So for 'Problem3', if we want to see the output instead of our program to stop abruptly, we can use a 'try-except' 

# Following the same procedure as Problem3:
s = set()

# Now, lets ask a user to input the values.

for i in range(3): 
    value = input("Input the desired value: ")
    s.add(value)

print(s)            # For inputs: 4, 5, 6; Output: {'4', '6', '5'}

my_list = [50, 60]
try:
    s.add(my_list)
except TypeError:
    print("You can't add a list to a set because it's unhashable.")


# Another example:
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except:
    print("Oops! Something went wrong.")

# For any other input other than int (like string), this program will return "Oops! Something went wrong." instead of throwing a conversion error.
# For '0' as input, this program will return "Oops! Something went wrong." instead of throwing a division by zero error.

# What is try-except?
# In Python, try-except is a way to handle errors without breaking your program. It’s like telling Python:

# "Try to run this code. If something goes wrong (an error), catch it and handle it nicely instead of crashing."