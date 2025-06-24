# Like lists, loops can also be used with strings.

# Lets write a program to ask user to enter that name of their city and then print every letter one by one.
city = input("Please eneter the name of your city: ") 

# Now let's print the letters of the entered city one by one. 
for letters in city:
    print(letters)

# Deep Dive:
# An example where this method can be useful is if we want to count the no. of vowels and consonents.
vowels = ["a", "e", "i", "o", "u"]
vowel_count = 0
consonant_count = 0

for alphabet in city:
    if alphabet in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print(f"The count of vowels in the city's name is {vowel_count}")
print(f"The count of consonants in the city's name is {consonant_count}")