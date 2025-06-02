# Q.1: Add two numbers entered by the user.

# Let's take two variable a & b.
# Use 'input()' function to ask user the numbers

a = input("Enter the 1st no.") 
b = input("Enter the 2nd no.")

# print(a+b) If we did this, the output will be 'ab' (concatinated).

# Ex: If a = 21 & b = 1, print(a+b) will return 211.
# Reason: Input function considers all inputs as "Strings"
# To add the numbers, first we will have to convert them to Integers. 

#Convert both to integers
sum = int(a)+int(b)

print("The sum of the numbers is", sum)