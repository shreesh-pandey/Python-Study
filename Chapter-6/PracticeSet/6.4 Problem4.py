# Q.4: Write a Python program to detect whether a given comment is spam or not. A comment is considered spam if it contains any of the following phrases:  
    
    # - "make a lot of money"
    # - "buy now"
    # - "subscribe this"
    # - "click this"
    
# The program should ask the user to enter a comment and check whether it contains any of the spam keywords (case-insensitive).
    
    # - If it does, print "This comment is spam."
    # - Otherwise, print "This comment is not spam."

# Lets start with asking user to input the comment.
comment = input("Please enter your comment: ").lower()

# Now lets create a list that contains all the spam comments.
spam = ["make a lot of money", "buy now", "subscribe this", "click this"]

# Now, lets use for loop along with a if statement to check if the comment contains any spam message.
for i in range (len(spam)):
    if spam[i] in comment:
        print("This comment is spam.")
        break
else:                       # This else belongs to the 'for' loop, not the 'if'
        print("This comment is not spam.")

# There is one another way to do it with same logic but without using indexing.
for phrase in spam:         # Replacing i with phrase to avoid confusion.
    if phrase in comment:
        print("This comment is spam.")
        break
else:
    print("This comment is not spam.")
