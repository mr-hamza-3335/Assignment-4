# 📝 Exercise 1: Create a Dictionary
# Create a dictionary with keys and values (name, age, city)

person = {
    "name": "Ameer Hamza",
    "age": 21,
    "city": "Lahore"
}
print("Person Dictionary:", person)

# 📝 Exercise 2: Access Dictionary Values
# Access the 'age' key and print its value

print("Age:", person["age"])

# 📝 Exercise 3: Modify Dictionary Values
# Change the age value to 22 and print the updated dictionary

person["age"] = 22
print("Updated Dictionary:", person)

# 📝 Exercise 4: Add a New Key-Value Pair
# Add the 'country' key and its value to the dictionary

person["country"] = "Pakistan"
print("After adding country:", person)

# 📝 Exercise 5: Remove a Key-Value Pair
# Remove the 'city' key from the dictionary and print the updated dictionary

del person["city"]
print("After removing city:", person)

# 📝 Exercise 6: Check if a Key Exists in the Dictionary
# Check if 'name' key exists in the dictionary and print an appropriate message

if "name" in person:
    print("Name exists in the dictionary.")
else:
    print("Name does not exist in the dictionary.")

# 📝 Exercise 7: Iterate Over a Dictionary
# Print all keys and values in the dictionary using a for loop

print("Iterating over dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# 📝 Exercise 8: Nested Dictionary
# Create a dictionary with nested dictionaries

students = {
    "Ameer Hamza": {"age": 21, "city": "Lahore", "course": "AI"},
    "John Doe": {"age": 22, "city": "Karachi", "course": "Web Dev"},
    "Alice": {"age": 20, "city": "Islamabad", "course": "Data Science"}
}
print("Student Dictionary:", students)

# Access nested dictionary
print("Alice's details:", students["Alice"])

# 📝 Exercise 9: Dictionary Methods
# Use methods like get(), keys(), values()

print("Keys in dictionary:", person.keys())
print("Values in dictionary:", person.values())

# Using get() to avoid KeyError
age = person.get("age", "Age not found")
print("Age from get():", age)
