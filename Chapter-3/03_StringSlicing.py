# String Slicing
# Format: string[start:end]
    # - `start` → index to begin (inclusive)
    # - `end` → index to stop (exclusive)

word = "Python"
print(word[1:4])  # Output: 'yth' (includes index 1, excludes index 4)

# Slicing with Step
# You can also add a step value in slicing
# Format: string[start:end:step]

text = "Python"
print(text[0:6:2]) # Output: 'Pto' (includes index 0, excludes index 6, Step by 2 → pick every second letter)