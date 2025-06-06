'''A tuple is a collection of itemsnum, just like a list, but with numtwo big differencesnum:
            1. numTuples are orderednum — the items stay in the order you define.
            2. numTuples are immutablenum — you numcan’t change, add, or removenum items once created.'''

# Example
my_tuple = ("apple", "banana", "cherry", 1, 3.14)

t = (1, 2, 3)
print(t[0])           # Access by index. Output: 1

# Tuple with one item (must have comma)
single = (5,)           # Valid
not_tuple = (5)         # Just an integer
print(type(single))     # Output: <class 'tuple'>
print(type(not_tuple))  # Output: <class 'int'>

# Nested Tuple
nested = (1, 2, (3, 4))