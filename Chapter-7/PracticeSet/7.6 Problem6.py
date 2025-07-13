# Q.6: Write a program that asks the user to keep entering numbers until they enter 0, then print the total.

# Initialize the sum

total = 0

# Start the loop
while True:
    number = int(input("Please enter a number (enter 0 to stop): "))
    if number == 0:
        break
    total += number

# Print the result
print(f"The sum of the numbers is: {total}")
