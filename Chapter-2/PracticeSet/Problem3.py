# Q.3: Check the type of variable received via input().

# Lets take a variable a.
# Lets use input() function to ask the input from user.

a = input("Input the variable a: ")

# Lets take another variable b.

b = input("Input the variable b: ")

# Lets take one more variable c.

c = input("Input the variable c: ")

# Another one as variable d.

d = input("Input the variable d: ")

# Since input() function takes all inputs as "Strings", the type of all of them will be "String".
# To include variety, lets convert b to type Integer, c to type Float, d to type Boolean

b = int(b)
c = float(c)
d = bool(d)

# Now lets check the types of the variables.

print(type(a))
print(type(b))
print(type(c))
print(type(d))


# Result:

# For these inputs:

# Input the variable a: 5
# Input the variable b: 2
# Input the variable c: 6
# Input the variable d: 1

# The output will be:

# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>