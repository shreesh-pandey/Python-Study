# Lets write a program that prints the table of 5 from 1 to 10.
print("Printing the table of 5 as below ...")

for i in range (11):
    print(f"5 * {i} = {5*i}")

# To understand 'for' loop better, lets Write a program that asks the user for a number n and then adds all numbers from 1 to n. Finally, print the total total.
# Lets ask the user to input the number.
n = int(input("Please enter the number: "))

# Now lets use for loop to add the numbers from '0' to 'n'.
total = 0
for i in range(1, n+1):         # n+1 as the stop parameter will stop at 'n' and will not include it.
    total += i

print(f"The total of numbers from 1 to {n} is: {total}")
