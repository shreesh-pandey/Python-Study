my_dict = {
    "name": "Shreesh",
    "age": 30,
    "country": "India"
}

# Keys: name, age, and country.
# Values: Shreesh, 30, and India.

print(my_dict)


# Accessing Data from Dictionary

print(my_dict["name"])     # Output: Shreesh
print(my_dict["age"])      # Output: 30


# Adding or Changing Values

my_dict["age"] = 36              # Update value
my_dict["profession"] = "PM"     # Add new key-value pair

print(my_dict)


# Removing Data

del my_dict["country"]

print(my_dict)

# Fun Fact: You can use Looping Through a Dictionary. Its a bit advanced so just read it as we will discuss it later in detail.

for key, value in my_dict.items():
    print(key, "→", value)
    
# Output:
# name → Shreesh
# age → 30
# country → India