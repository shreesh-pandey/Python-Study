# Lets write a program that takes the number from the user and prints the multiplication table for it.
# Lets start with asking the user for the number.
number = int(input("Please enter the number you want to see the table for: "))

# Now lets use while loop to print the table for the entered number.
i = 1
print(f"Printing the multiplication table for {number}/n")
while i <= 10:
    print(f"{number} * {i} = {number*i}")
    i += 1

# Let's write a program that keeps asking the user to guess a number until they guess it correctly.
# They will get a maximum of 3 chances.

# Step 1: Set the secret number
secret_number = 3

# Step 2: Print game instructions
print("🎮 Welcome to the Guessing Game!")
print("You need to guess a number between 1 to 10.")
print("You have 3 chances. Let's see if you can guess it!")

# Step 3: Loop to give user 3 chances
for i in range(1, 4):
    guess = int(input(f"Chance {i}: Please enter your guess: "))
    
    if guess == secret_number:
        print("🎉 Congratulations! You guessed it right! You win!")
        break
    else:
        print("❌ Wrong guess! Try again.")
        if i == 3:
            print("😔 You've used all your chances. Better luck next time!")

# Future tasks:
# Turn this into a random number guessing game.
# Let the user play again (using a loop).
# Add hints (e.g., “Too high” or “Too low”).
# Track how many attempts the user needed.