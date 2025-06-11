person = {"name": "Shreesh", "age": 30, "city": "Delhi"}

# To return a list-like view of all the keys.
print(person.keys())       # dict_keys(['name', 'age', 'city'])

# To return a list-like view of all the values.
print(person.values())     # dict_values(['Shreesh', 30, 'Delhi'])

# To return the value of the specified key, or None if key not found
print(person.get("name"))  # Shreesh
print(person.get("job"))   # None

# To add or update key-value pairs from another dictionary
person.update({"age": 31})
print(person)              # {'name': 'Shreesh', 'age': 31, 'city': 'Delhi'}

# To remove the specified key and returns its value
person.pop("city")
print(person)              # {'name': 'Shreesh', 'age': 31}