# Q.2: Write a program to accept marks om 6 students and display them in a sorted manner.

# First we have to define a list where we will store the provided marks.
marks = []         # Empty list

# Lets use input() function to ask the marks.
m1 = input("Enter the marks: ")

# To add it to the list, we will use append() function
marks.append(m1)    # This will add the given marks to the list.

# We will repeat it five more times.
m2 = input("Enter the marks: ")
marks.append(m2)
m3 = input("Enter the marks: ")
marks.append(m3)
m4 = input("Enter the marks: ")
marks.append(m4)
m5 = input("Enter the marks: ")
marks.append(m5)
m6 = input("Enter the marks: ")
marks.append(m6)

print(marks)       # Output: ['78', '52', '98', '89', '48', '89']

# Now lets use sort() function to sort it.

marks.sort()
print(marks)       # Output: ['48', '52', '78', '89', '89', '98']

# Fun Fact: We can use loops to do it more efficiently. But it is a bit advance so just read it as we will discuss it in future in detail.

num = []  # Empty list.

# For loop
for i in range(1,7):
    m = input("Enter the marks: ")
    num.append(m)

print(num)       # Output: ['78', '52', '98', '89', '48', '89']

num.sort()
print(num)       # Output: ['48', '52', '78', '89', '89', '98']