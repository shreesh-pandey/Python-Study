# Q.3: Create a program that explores how sets handle uniqueness and different data types.
#     What Your Program Should Do: 
#     - Ask the user to input 3 values one by one (can be numbers or strings).
#     - Store these values in a set and display all the unique values.
#     - Then, manually try to add both 18 (int) and '18' (str) to the set. Show that both are stored because they are different types.
#     - Add the values 20, 20.0, and '20' to the set and display its length.
#     - Attempt to add a list as a set element and display the output.
#     - In the end, print the final set.

# Lets start with creating an empty set.
s = set()

# Now, lets ask a user to input the values.

for i in range(3): 
    value = input("Input the desired value: ")
    s.add(value)

print(s)            # For inputs: 4, 5, 6; Output: {'4', '6', '5'}

# Now, lets manually add both `18` (int) and `'18'` (str) to the set.
s.add(18)
s.add('18')
print(s)            # For inputs: 4, 5, 6; Output: {'6', '18', 18, '5', '4'}

# Now, Lets add the values 20, 20.0, and '20' to the set and display its length.
s.add(20)
s.add(20.0)
s.add('20')
print(s)            # For inputs: 4, 5, 6; Output: {'4', '5', '20', '18', '6', 18, 20}
print(len(s))       # For inputs: 4, 5, 6; Output: 7

# 20 and 20.0 are considered equal in Python because they have the same value.
# Hence, only one of them will be added to the set.

# Now, lets try to add a list as a set element and display the output.
my_list = [50, 60]
s.add(my_list)
print(s)            # Output: TypeError: unhashable type: 'list'. Because we can't add list to a set as they are unhashable type.

# Since we can't add lists to a set, hence. for inputs: 4, 5, 6; Output: {'4', '5', '20', '18', '6', 18, 20} is the final set.

