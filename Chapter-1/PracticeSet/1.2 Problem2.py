# Q: Print the table of 5.

# A simple way is to print everything one by one:

print("5 x 1 = 5")
print("5 x 2 = 10")
print("5 x 3 = 15")
print("5 x 4 = 20")
print("5 x 5 = 25")
print("5 x 6 = 30")
print("5 x 7 = 35")
print("5 x 8 = 40")
print("5 x 9 = 45")
print("5 x 10 = 50")

# Another way is to print using loops like while and for:

# Using while loop

i = 1
while i <= 10:
    print("5 x", i, "=", 5 * i)
    i = i + 1

# Using for loop

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# Future Task:
# Make it dynamic — ask the user for a number and print its multiplication table.