# List methods are built-in functions that help you manipulate lists — like adding, removing, or sorting items.

num = [1, 2, 3, 4, 5]

# Examples
# append() adds the item at the end
num.append(6)
print(num)          # Output: [1, 2, 3, 4, 5, 6]

# insert(index, item) adds the item at the specified index
num.insert(1, 7)
print(num)          # Output: [1, 7, 2, 3, 4, 5, 6]

# remove(), removes the item from the list
num.remove(4)
print(num)          # Output: [1, 7, 2, 3, 5, 6]

# pop() removes item at given index (or last if none given)
print(num.pop())    # Output: 6
print(num)          # Output: [1, 7, 2, 3, 5]

# sort() sorts the items of the list list in ascending order
num.sort()
print(num)          # Output: [1, 2, 3, 5, 7]

# reverse(), reverses the order of the items in the list
num.reverse()
print(num)          # Output: [7, 5, 3, 2, 1]