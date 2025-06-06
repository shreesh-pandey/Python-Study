# Q.3: Check that a tuple type cannot be changed in python.

# Lets create a tuple
a = (54, 89, "Shree", "Rubai")

# Lets print the tuple to check.
print(a)            # Output: (54, 89, 'Shree', 'Rubai')

# Lets try to change the name Rubai to Pritha.
a[3] = "Pritha"
print(a)            # TypeError: 'tuple' object does not support item assignment