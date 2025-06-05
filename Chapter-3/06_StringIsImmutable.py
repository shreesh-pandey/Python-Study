# String is immutable

name = "Shreesh"
name[0] = "P"   # This will give an error! 'TypeError: 'str' object does not support item assignment'

# However, you can create a new string using parts of the old one.
new_name = "P" + name[1:]
print(new_name) # Output: "Phreesh"