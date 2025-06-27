# Loops can also be used with lists.
# To understand, lets start with creating a list of names.
names = ["Shreesh", "Pritha", "Rubai", "Sultana"]
for name in names:
    print(name)

# The Outpput for this program will be:
# Shreesh
# Pritha
# Rubai
# Sultana


# Lets make a program that asks a user to enter their 5 favorite programing languages and print them.
# Without loops we will write something like this:

language = []

fav_lang1 = input("Input your first favorite language: ")
language.append(fav_lang1)
fav_lang2 = input("Input your second favorite language: ")
language.append(fav_lang2)
fav_lang3 = input("Input your third favorite language: ")
language.append(fav_lang3)
fav_lang4 = input("Input your fourth favorite language: ")
language.append(fav_lang4)
fav_lang5 = input("Input your fifth favorite language: ")
language.append(fav_lang5)

# Then we will print them.
print(language)

# With loops, it can be done in very short like this:
favorite_languages = []

for i in range(1, 6):
    fav_lang = input(f"Please enter your favorite language no. {i}: ")
    favorite_languages.append(fav_lang)

print(favorite_languages)

# To print languages seperately instead of a list form we can use loops as well:
for lang in favorite_languages:
    print(lang)
