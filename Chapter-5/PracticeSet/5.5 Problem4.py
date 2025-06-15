# Q.4: Create a Python program that:

# Starts with an empty dictionary. Asks 4 users (friends) to enter:
#   - Their name (used as the key)
#   - Their favorite language (used as the value)

# And then stores these name-language pairs in the dictionary.

# Also handle and understand:
#   - What happens if two users enter the same name?
#   - What happens if two users enter the same favorite language?

# Lets start with creating an empty dictionary.
d = {}

# Now lets update the dictionary by asking the users for their names and favorite language.
for i in range(4):
    name = input("What is your name?: ")
    lang = input("What is your favorite language?: ")
    d.update({name: lang})

print(d)            # Output: {'Shreesh': 'Python', 'Pritha': 'Python', 'Rubai': 'C++', 'Sultana': 'Java'}

# If two users enter the same name, the program will update the value of the old key (name) with the new one.
# Example: If in the above program, we enter Pritha as name once again and then enter the language as Java, the value of Pritha will change to Java.

new_dict = {}

# Now lets update the dictionary by asking the users for their names and favorite language.
for i in range(4):
    name = input("What is your name?: ")
    lang = input("What is your favorite language?: ")
    new_dict.update({name: lang})

print(new_dict)            # Output: {'Shreesh': 'Python', 'Pritha': 'Java', 'Rubai': 'C++'}

# If two users enter the same favorite language, it's fine as values can be same for different keys. Its the keys that needs to be unique.
# This is apparant from the output in the first program: Output: {'Shreesh': 'Python', 'Pritha': 'Python', 'Rubai': 'C++', 'Sultana': 'Java'}