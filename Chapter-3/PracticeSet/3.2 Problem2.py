# Q.2: Write a program to fill in a letter template given below with name and date.
    # letter = ''' Dear <|Name|>,
    # You are selected!
    # <|Date|> '''

# Lets start with the input function to ask the name

name = input("Hi! Please tell me your name: ")

# Now, lets use variable a to declare the multi-line string
a =  ''' Dear <|Name|>,
    You are selected!
    <|Date|> '''

# Now, lets use replace() fuction to change the relevant strings to desired strings
Letter = a.replace("<|Name|>",name).replace("<|Date|>","June 06,2020")
print(Letter)

# Fun Fact: We can also automate this letter to fetch todays date whenever it runs by importingg 'datetime' library
import datetime

name = input("Hi! Please tell me your name: ")
a = '''Dear <|Name|>,
You are selected!
<|Date|>'''

# Get today's date
today = datetime.date.today()

# Replace placeholders
letter = a.replace("<|Name|>", name).replace("<|Date|>", str(today))

print(letter)

# Another example: template = "Hi <|Name|>! It's great to know that you love <|Language|>."
# Lets start with the input function to ask the name and language

name = input("Hi! Please tell me your name: ")
lang = input("Hi! Please tell me the language you love: ")

# Now, lets use variable a to declare the string template
b = "Hi <|Name|>! It's great to know that you love <|Language|>."

# Now, lets use replace() fuction to change the relevant strings to desired strings
template = b.replace("<|Name|>",name).replace("<|Language|>",lang)
print(template)


