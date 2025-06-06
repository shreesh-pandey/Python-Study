# Q.4: Write a program to sum a list with 4 numbers.

# Leta start with making a list.
lst = [5, 6, 8, 7, 9]

# To add the numbers in the list, we will use indexing.
# Lets assign the value at each index to a variable.
a = lst[0]
b = lst[1]
c = lst[2]
d = lst[3]
e = lst[4]

# Now lets add these variables and assign the sum to another variable named 'total'
total = a+b+c+d+e

# Print total
print(total)

# Another way is to use the inbuilt sum fuction.
lst = [5, 6, 8, 7, 9]
total = sum(lst)            # Using sum() function.
print(total)                # Print total

# A more advanced way is to use for loop
# Lets define the list
my_list = [5, 6, 8, 7, 9]

# Lets use a variable named total in which we will assign the sum.
total = 0

# Lets use for loop while using 'i' as an incremental variable that will use start from the value of index 0 to the end of the list.
for i in my_list:
    total += i

print(total)

# Another way do the same thing id=s with index using a for loop and range().

my_list = [5, 6, 8, 7, 9]

total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)


