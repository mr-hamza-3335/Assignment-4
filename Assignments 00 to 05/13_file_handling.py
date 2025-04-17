# 📝 Exercise 1: Write to a File
# Open a file in write mode and write some text into it

with open("example.txt", "w") as file:
    file.write("Hello, this is a test file!\n")
    file.write("Python file handling is easy.\n")

print("Text written to example.txt")

# 📝 Exercise 2: Read from a File
# Open the file in read mode and print its content

with open("example.txt", "r") as file:
    content = file.read()
    print("Content of example.txt:\n", content)

# 📝 Exercise 3: Append to a File
# Open a file in append mode and add more text

with open("example.txt", "a") as file:
    file.write("Adding more content to the file.\n")
    file.write("File handling is great!\n")

print("Text appended to example.txt")

# 📝 Exercise 4: Read a File Line by Line
# Open the file and read it line by line using a for loop

print("Reading file line by line:")
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes extra whitespace

# 📝 Exercise 5: Handle File Not Found Error
# Try to read from a non-existing file and handle the exception

try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file was not found.")

# 📝 Exercise 6: Write Multiple Lines to a File
# Write a list of strings to a file, each on a new line

lines = ["Line 1: This is the first line.\n", "Line 2: This is the second line.\n", "Line 3: This is the third line.\n"]
with open("multi_lines.txt", "w") as file:
    file.writelines(lines)

print("Multiple lines written to multi_lines.txt")

# 📝 Exercise 7: File Operations - Rename or Delete a File
# Rename a file and then delete it

import os

os.rename("multi_lines.txt", "renamed_file.txt")
print("File renamed to renamed_file.txt")

os.remove("renamed_file.txt")
print("File renamed_file.txt has been deleted.")
