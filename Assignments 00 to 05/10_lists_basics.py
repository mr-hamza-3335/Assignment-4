# 📝 Exercise 1: Create and Print a List
# Create a list of your favorite fruits and print it

fruits = ["Apple", "Banana", "Mango", "Orange", "Pineapple"]
print("Favorite Fruits:", fruits)

# 📝 Exercise 2: Access List Elements
# Access and print the second item from the list

print("Second fruit in the list:", fruits[1])

# 📝 Exercise 3: Modify List Elements
# Change the first fruit in the list to "Grapes" and print the updated list

fruits[0] = "Grapes"
print("Updated fruits list:", fruits)

# 📝 Exercise 4: Add Elements to the List
# Add a new fruit to the end of the list using append() and print the list

fruits.append("Watermelon")
print("After adding watermelon:", fruits)

# 📝 Exercise 5: Remove an Item from the List
# Remove the fruit "Mango" from the list and print the updated list

fruits.remove("Mango")
print("After removing Mango:", fruits)

# 📝 Exercise 6: Slicing the List
# Print the first 3 fruits from the list using slicing

print("First 3 fruits:", fruits[:3])

# 📝 Exercise 7: Iterate Over a List
# Use a for loop to print each fruit in the list

print("List of Fruits:")
for fruit in fruits:
    print(fruit)

# 📝 Exercise 8: Nested List
# Create a list of lists (for example, a list of students' names and their ages)

students = [["Ameer Hamza", 21], ["John Doe", 22], ["Alice", 20]]
print("List of Students and their Ages:")
for student in students:
    print(f"Name: {student[0]}, Age: {student[1]}")
