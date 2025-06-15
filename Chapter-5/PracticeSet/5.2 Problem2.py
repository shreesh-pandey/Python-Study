# Q.2: Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up! Use a different approach.

# In the program that we created in 5.1, we can only input one word and it's meaning in the dictionary.
# However, we can make it better by allowing it to use multiple inputs by using for loop.
# For that, lets start with creating the dictionary.

my_dict = {}

# Since we have to have an end range while inputing the words, lets ask the user how many words they want to update.
count = input("How many words do you want to update: ")
for i in range(int(count)):
    hindi_word = input("Input the Hindi word: ")
    english_meaning = input("Input it's English meaning: ")
    my_dict.update({hindi_word:english_meaning})

# Now lets solve the problem by allowing user to look up the translation.
search_word = input("Input the Hindi word you want to lookup: ")
print(my_dict.get(search_word, "Sorry! The word was not found."))
