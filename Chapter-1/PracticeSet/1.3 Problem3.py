# # Q: Install an external module and use it to perform an operation of your interest.

# A good beginner-friendly module is 'pyjokes' (it gives random programming jokes).

import pyjokes

joke = pyjokes.get_joke()
print("Here's a joke for you:")
print(joke)


# Another good beginner-friendly module is 'emojis' File name: emojis.py

import emoji

print(emoji.emojize("Python is fun :snake:", language='alias'))
print(emoji.emojize("Keep going! :rocket:", language='alias'))
print(emoji.emojize("You're doing great! :thumbs_up:", language='alias'))

# Lets dial up a little and check a very interesting module 'pyttsx3'

import pyttsx3

engine = pyttsx3.init()
engine.say("Hey I am good")
engine.runAndWait()