# Q.8: Print all even numbers between 1 and 100.

print("Even numbers from 1 to 100 are:")
for i in range (1, 101):
    if i%2 == 0:
        print(f"{i}")


# -------------------------- -------------------------- -------------------------- #


# Deep Dive

# We can make this code better like this:

for i in range(2, 101, 2):
    print(i)

# Why is it better?
# Because we are directly looping over even numbers, avoiding the unnecessary 'if i % 2 == 0 check'.



