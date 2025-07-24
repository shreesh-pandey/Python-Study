# Q.7: Count and print how many vowels are in a string entered by the user.

# Ask the user to enter a string
user_input = input("Please enter a string: ").lower()

# Define the vowels (lowercase and uppercase)
vowels = "aeiou"

# Initialize the counter
vowel_count = 0

# Loop through each character in the string
for char in user_input:
    if char in vowels:
        vowel_count += 1

# Print the total number of vowels
print(f"The total number of vowels in the string is: {vowel_count}")


