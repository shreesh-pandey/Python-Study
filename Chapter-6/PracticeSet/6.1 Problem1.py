# Q.1: Write a program to find the greatest of four numbers entered by the user.

# Lets start with asking user to input four numbers.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

if(a>b and a>c and a>d):
    print("Greatest number is a:", a)

elif(b>a and b>c and b>d):
    print("Greatest number is b:", b)

elif(c>a and c>b and c>d):
    print("Greatest number is c:", c)

else:
    print("Greatest number is d:", d)

# We can also do this without using only 'if' statement without using 'else':

# Lets ask the user to enter four numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

# Start by assuming the first number is the greatest
greatest = a

# Compare with b
if b > greatest:
    greatest = b

# Compare with c
if c > greatest:
    greatest = c

# Compare with d
if d > greatest:
    greatest = d

# Show the result
print("The greatest number is:", greatest)
