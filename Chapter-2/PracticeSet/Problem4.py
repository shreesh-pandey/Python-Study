# Q.4: Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not. Take a = 34 and b = 80

# Lets take a variable a.
# Lets use input() function to ask the input from user.

a = input("Input the variable a: ")

# Lets take another variable b.

b = input("Input the variable b: ")

# Since we are going to use numbers, lets change them first and then do the comparision.

a = int(a)
b = int(b)

# Now lets compare them according to our question.

print(a == b) # Since we are taking a as 34 and b as 80, the Output will be 'False'

# Another way to do it is by assigning the result to a variable and then printing the variable.

c = (a == b)
print(c)