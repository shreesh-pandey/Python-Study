# Q.3: Write a program to detect double space in a string.
# Lets use a variable to declare the string.
a = "This is a string with  double space."

# Now lets use find() string methos to find "  "
print(a.find("  "))

# Now lets replace the double space with single spaces.
print(a.replace("  "," "))
