# Common String Methods/Functions

name = "  Shreesh  "
print(name.strip())  # Removes spaces → "Shreesh"
print(name.upper())  # ALL CAPS → "  SHREESH  "

str = "python is fun"
print(str.title())  # ALL CAPS → "Python Is Fun"

# These methods can be chained together too!

a = "   hello world   "

# Step by step method

# First, strip the white space
print(a.strip()) # Output: hello world

# Second, replace 'hello' with 'hi'
print(a.replace("hello", "hi")) # Output: hi world

# Third, make first letters capital.
print(a.title()) # Output: Hello World. 'Because string is immutable.

# Chained method

a = "   hello world   "
print(a.strip().replace("hello", "hi").title()) # Output: 'hi world'
