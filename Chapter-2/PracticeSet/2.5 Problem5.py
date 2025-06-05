# Q.5: Write a python program to find an average of two numbers entered by the user.

# Lets start with variables. We will use input() function to ask for the numbers.

# First no.
a = input("Input the 1st no.: ")

# Second no.
b = input("Input the 2nd no.: ")

# Since input() function considers every input as string, we will need to change them to integer
a = int(a)
b = int(b)

# To find the average of the number, we will use the formula (a+b)/2
# Lets take a third variable 'avg'
avg = (a+b)/2

# To get the output, we need to print it.
print("The average of the numbers is: ", avg)

# We can also combine the steps and convert the input into integers within the formula
avg = (int(a)+int(b))/2

# To get the output, we need to print it.
print("The average of the numbers is: ", avg)