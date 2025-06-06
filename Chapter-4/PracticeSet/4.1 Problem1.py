# Q.1: Write a program to store seven fruits in a list entered by the user.

# First we have to define a list where we will store the names of the provided fruits.
fruits = []         # Empty list

# Lets use input() function to ask the fruit's name.
f1 = input("Enter the fruit name: ")

# To add it to the list, we will use append() function
fruits.append(f1)    # This will add the given fruit's name to the list.

# We will repeat it for six more times.
f2 = input("Enter Fruit name: ")
fruits.append(f2)
f3 = input("Enter Fruit name: ")
fruits.append(f3)
f4 = input("Enter Fruit name: ")
fruits.append(f4)
f5 = input("Enter Fruit name: ")
fruits.append(f5)
f6 = input("Enter Fruit name: ")
fruits.append(f6)
f7 = input("Enter Fruit name: ")
fruits.append(f7)

print(fruits)       # Output: ['apple', 'banana', 'peach', 'pear', 'mango', 'papaya', 'strawberry']

# Fun fact: We can use loops to do it more efficiently. But it is a bit advance so just read it as we will discuss it in future in detail.

for i in range(1,8):
    f = input("Enter the fruit name: ")
    fruits.append(f)

print(fruits)       # Output: ['apple', 'banana', 'peach', 'pear', 'mango', 'papaya', 'strawberry']