# Lets write a simple if-else program to check if a number is even or odd.
num = int(input("Enter the number: "))

if(num%2==0):
    print("The number is Even! Thank you!")
else:
    print("The number is Odd! Thank you!")

# Here, we can write this if else program in a sigle line with Conditional Expressions.
# Syntax: <value_if_true> if <condition> else <value_if_false>
print("The number is Even! Thank you!") if(num%2==0) else print("The number is Odd! Thank you!")
