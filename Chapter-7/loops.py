# Lets say we want to write our name 5 times
# Lets start with asking the user to input the name.

name = input("Please enter your name: ")

# Now lets print it for 5 times.
print(name)
print(name)
print(name)
print(name)
print(name)

# It is feasible as the repeatations are low. But what if we have to print it for 100 times?
# That's where loops are useful. The above code can be written in short with loops like:

for i in range(5):
    print(name)
