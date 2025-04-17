# 📝 Exercise 1: Basic Info from User
# Ask the user for name and age and print a greeting

name = input("What is your name? ")
age = input("What is your age? ")
print(f"Hello {name}, you are {age} years old!")

# 📝 Exercise 2: Ask favorite programming language
language = input("Which programming language do you like? ")
print(f"{language} is a great choice!")

# 📝 Exercise 3: Simple calculator
# Ask user for two numbers and add them

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert to integers
num1 = int(num1)
num2 = int(num2)

sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}")

# 📝 Exercise 4: Multiplication Table
# Ask a number and print its multiplication table

table_num = int(input("Enter a number for multiplication table: "))
print(f"Multiplication table of {table_num}:")
for i in range(1, 11):
    print(f"{table_num} x {i} = {table_num * i}")

# 📝 Exercise 5: Formatted sentence
# Ask user for city and favorite food and print a sentence

city = input("Which city are you from? ")
food = input("What's your favorite food? ")
print(f"{name} is from {city} and loves eating {food}.")
