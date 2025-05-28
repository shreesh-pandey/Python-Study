# Type Checking and Typecasting

a = "31.2"
b = float(a) # a but the type should be float
t = type(b) 

print(t)

# More Examples:

# Convert string to integer
num = int("10")
print(num + 5)  # Output: 15

# Convert float to integer
a = int(3.99)
print(a)  # Output: 3

# Convert integer to string
age = 25
print("Age: " + str(age))  # Output: Age: 25

# Convert list to set
nums = [1, 2, 2, 3]
unique_nums = set(nums)
print(unique_nums)  # Output: {1, 2, 3}