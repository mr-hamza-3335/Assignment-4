# lists_and_dicts.py
# Author: Ameer Hamza - Age: 21 - GIAIC Student

# Lists Example
fruits = ["apple", "banana", "orange"]
print("List of fruits:", fruits)
fruits.append("grape")
print("After adding grape:", fruits)

# Accessing list element
print("First fruit:", fruits[0])

# Dictionaries Example
student = {
    "name": "Ameer Hamza",
    "age": 21,
    "course": "AI"
}

print("Student Information:", student)
student["age"] = 22  # Update age
print("Updated student information:", student)

# Adding a new key-value pair
student["city"] = "Lahore"
print("Student with city added:", student)
