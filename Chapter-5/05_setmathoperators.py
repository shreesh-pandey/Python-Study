# Lets create two sets 'a' & 'b'
a = {1, 2, 3}
b = {3, 4, 5}

# Union Method:
# Syntax: (set1 | set2) or (set1.union(set2))
# Combines all elements from both sets. No duplicates.
print(a | b)             # Output: {1, 2, 3, 4, 5}
print(a.union(b))        # Same as above

# Intersection Method:
# Syntax: (set1 & set2) or (set1.intersection(set2))
# Gives only the common elements between sets.
print(a & b)             # Output: {3}
print(a.intersection(b)) # Same

# Difference Method:
# Syntax: (set1 - set2) or (set1.difference(set2))
# Returns items only in set1, not in set2.
print(a - b)             # Output: {1, 2}
print(a.difference(b))   # Same

# Symmetric Difference Method:
# Syntax: (set1 ^ set2) or (set1.symmetric_difference(set2))
# Returns items in either set, but not in both.
print(a ^ b)                   # Output: {1, 2, 4, 5}
print(a.symmetric_difference(b))  # Same

# Subset Method:
# Syntax: (set1 <= set2) or (set1.issubset(set2))
# Checks if all elements of `set1` are in `set2`.
print(a <= b)                 # False
print(a.issubset(b))          # False

# Superset Method:
# Syntax: (set1 >= set2) or (set1.issuperset(set2))
# Checks if `set1` contains all elements of `set2`.
print(a >= b)                # False
print(a.issuperset(b))       # False

# Disjoint Method:
# Syntax: (set1.isdisjoint(set2)0)000000000000000000000000
# Returns `True` if sets have no elements in common, else returns 'False'
print(a.isdisjoint(b))       # False