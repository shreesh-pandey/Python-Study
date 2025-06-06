# Since tuples are immutable (you can’t change them after creation), they have very few built-in methods but only the ones that do not modify the tuple.

# count() method
# Returns the number of times a value appears in the tuple.
# Syntax: tuple_name.count(value)
# Example:

fruits = ("apple", "banana", "apple", "cherry")
print(fruits.count("apple"))     # Output: 2


# index() method
# Returns the first index (position) where the value appears in the tuple.
# Syntax: tuple_name.index(value)
# Example:

numbers = (10, 20, 30, 20, 40)
print(numbers.index(20))        # Output: 1 (first occurrence)
