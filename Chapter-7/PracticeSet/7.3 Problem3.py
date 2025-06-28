# Q.3. Write a program that asks the user to enter a number and checks whether it is a prime number or not.
        # - If it's not a prime, display the reason (e.g. the first factor that proves it’s not prime).
        # - If it’s a prime, print a success message.
        # - Also, handle edge cases like numbers less than 2.

# -------------------------- -------------------------- -------------------------- #

# Solution:

# Ask the user to input a number to check for primality
number = int(input("Please enter the number to check if it's prime or not: ")) 

print("\nChecking result...\n")

# Prime numbers are greater than 1 and only divisible by 1 and themselves
if number < 2:
    print("The entered number is less than 2. Prime numbers start from 2.")
else:
    # Loop from 2 to number-1 to check if any number divides 'number' exactly
    for i in range(2, number):
        if number % i == 0:
            # If we find a divisor, it's not a prime number
            print(f"{number} is not a Prime Number because it is divisible by {i}.")
            break  # No need to continue checking
    else:
        # This else runs only if the loop completes without finding a divisor or if the loop doesn't run at all (in case of number == 2).
        print(f"The number you have entered is {number}, and it is a Prime Number!")


