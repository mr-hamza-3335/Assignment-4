# 📝 Exercise 1: Creating a Tuple
# Create a tuple with 5 elements and print it

my_tuple = ("apple", "banana", "cherry", "orange", "kiwi")
print("Tuple:", my_tuple)

# 📝 Exercise 2: Accessing Tuple Elements
# Access and print the second item in the tuple

print("Second item in tuple:", my_tuple[1])

# 📝 Exercise 3: Tuple Slicing
# Print the first 3 elements from the tuple using slicing

print("First 3 elements in tuple:", my_tuple[:3])

# 📝 Exercise 4: Nested Tuple
# Create a nested tuple and access an inner element

nested_tuple = (("John", 25), ("Alice", 23), ("Bob", 27))
print("Inner element of nested tuple:", nested_tuple[1][0])

# 📝 Exercise 5: Tuples and Immutability
# Try changing an element of the tuple (this should raise an error)

try:
    my_tuple[0] = "grape"  # This will raise a TypeError since tuples are immutable
except TypeError as e:
    print(f"Error: {e}")

# 📝 Exercise 6: Creating a Set
# Create a set of fruits and print it (duplicates will be removed)

fruit_set = {"apple", "banana", "cherry", "apple", "orange"}
print("Set of fruits:", fruit_set)

# 📝 Exercise 7: Add and Remove Items in a Set
# Add a new fruit to the set and remove an existing one

fruit_set.add("kiwi")
fruit_set.remove("banana")
print("Updated set of fruits:", fruit_set)

# 📝 Exercise 8: Set Operations
# Perform union and intersection between two sets

set1 = {"apple", "banana", "cherry"}
set2 = {"orange", "banana", "kiwi"}

# Union (all elements from both sets)
union_set = set1.union(set2)
print("Union of sets:", union_set)

# Intersection (common elements)
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

# 📝 Exercise 9: Checking Membership in a Set
# Check if a fruit is in the set

if "apple" in fruit_set:
    print("Apple is in the fruit set.")
else:
    print("Apple is not in the fruit set.")
