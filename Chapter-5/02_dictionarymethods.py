person = {"name": "Shreesh", "age": 30, "city": "Delhi"}

# Output: To return a list-like view of all the keys.
print(person.keys())       # Output: dict_keys(['name', 'age', 'city'])

# Output: To return a list-like view of all the values.
print(person.values())     # Output: dict_values(['Shreesh', 30, 'Delhi'])

# Output: To return the value of the specified key, or None if key not found
print(person.get("name"))  # Output: Shreesh
print(person.get("job"))   # Output: None

# Output: To add or update key-value pairs from another dictionary
person.update({"age": 31})
print(person)              # Output: {'name': 'Shreesh', 'age': 31, 'city': 'Delhi'}

# Output: To add key-value pairs from another dictionary
person.update({"profession": "PM"})
print(person)              # Output: {'name': 'Shreesh', 'age': 31, 'city': 'Delhi', 'profession': 'PM'}

# Output: To remove the specified key and returns its value
person.pop("city")
print(person)              # Output: {'name': 'Shreesh', 'age': 31, 'profession': 'PM'}