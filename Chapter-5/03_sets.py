my_set = {1, 2, 3}
print(my_set)  # Output: {1, 2, 3}

# Sets are Unique. It means if you try to add the same item more than once, it will only keep one.
my_set = {1, 2, 3, 2, 1}
print(my_set)  # Output: {1, 2, 3} → duplicates removed

# To create an emtpty set, we use set operator.
s = set()  # Create empty set
print(type(s))  # Output: <class 'set'>

# s = {} is a dictionary

# Although sets themselves are mutable, they cannot contain mutable elements like lists.
# This is because set elements must be hashable and immutable (so they can be compared and stored efficiently).
my_set = {1, 2, 3}
my_set.add((4, 5))      # Tuples are immutable so this works
print(my_set)           # Output: {(4, 5), 1, 2, 3}
my_set.add([6, 7])      # TypeError: unhashable type: 'list'