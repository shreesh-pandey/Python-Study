# Q.1: Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

# Although, we can solve this proble by creating a dictionary with pre-defined key-values, but let's make it better by making it dynamic.
# For that, lets create an empty dictionary.
my_dict = {}

# Now let's update the dictionary with the Hindi words and their English translation.
a = input("Input the Hindi word: ")
b = input("Input it's English meaning: ")

# Now lets update the dictionary 't' with the given inputs.
my_dict.update({a:b})
print(my_dict)

# Now lets solve the problem by allowing user to look up the translation.
translation = input("Input the Hindi word you want to lookup: ")
print(my_dict.get(translation, "Sorry! The word not found."))

# Deep Dive:
# Check 5.2 Problem2.py for a different approach to this problem.