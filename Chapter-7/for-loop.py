# To understand for loop, lets Write a program that asks the user for a number n and then adds all numbers from 1 to n. Finally, print the total total.
# Lets ask the user to input the number.
n = int(input("Please enter the number: "))

# Now lets use for loop to add the numbers from '0' to 'n'.
total = 0
for i in range(1, n+1):
    total += i

print(f"The total of numbers from 1 to {n} is: {total}")
