# Q.9: 9. Write a program to print the following star patterns based on user input `n`:
    # - A left-aligned triangle
        
    #     *
    #     **
    #     ***
        
    # - A centered pyramid
        
    #       *
    #      ***
    #     *****
        
    # - A square border (hollow square)
        
    #     * * *
    #     *   *
    #     * * *
  
# Ask user to Input the number
n = int(input("Please enter the number of stars to be printed: "))

# For left aligned pattern
for i in range(1, n+1):
    print("*"*i)
print("")

# For center aligned pattern
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1))
print("")

# For square border (hollow square)
for i in range(1, n+1):
    if(i==1 or i==n):
        print("*"*n)
    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*")
print("")

# Deep Dive

# Another way to write this code in a single line is by using f-string
# print("*", end="")
# print(" "*(n-2), end="")
# print("*")

# Like this:
# print(f"*{' ' * (n - 2)}*")

# Additionally, we can add a check to handle small values like when n < 2:
# if n < 2:
#     print("Size should be at least 2 to form a hollow square.")
# else:
#     # for loop here