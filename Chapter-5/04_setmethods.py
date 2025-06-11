# Lets create a set `s` with four numbers.

s = {1, 2, 3, 4}

# Add() Method:
s.add(5)        # Adds the number `5` to the set.
print(s)        # Output: {1, 2, 3, 4, 5}

# Remove() Method:

s.remove(2)     # Removes the element `2` from the set.
print(s)        # Output: {1, 3, 4}

# Important: If the item doesn’t exist, `remove()` gives an error.

# Pop() Method:
a = s.pop()     # Removes and returns a random item from the set (since sets are unordered)
print(a)        # Output might be any one of 1, 2, 3, 4, randomly

# Important: Use only when you don’t care which item is removed.


# Clear() Method:

s.clear()       # Empties the set (removes all items).
print(s)        # Output: set() → Empty set.