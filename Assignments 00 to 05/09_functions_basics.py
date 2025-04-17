# 📝 Exercise 1: Simple Function to Greet
# Define a function that prints a greeting message

def greet(name):
    print(f"Hello, {name}! Welcome to Python learning.")

greet("Ameer Hamza")

# 📝 Exercise 2: Function to Add Two Numbers
# Define a function that takes two numbers and returns their sum

def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(5, 7)
print(f"The sum of 5 and 7 is: {result}")

# 📝 Exercise 3: Function to Check Even or Odd
# Define a function that checks whether a number is even or odd

def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is an even number."
    else:
        return f"{num} is an odd number."

print(check_even_odd(21))
print(check_even_odd(42))

# 📝 Exercise 4: Function to Calculate Factorial
# Define a function that calculates the factorial of a number

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print(f"Factorial of 5 is: {factorial(5)}")

# 📝 Exercise 5: Function with Default Argument
# Define a function with a default argument for greeting

def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user()  # Will use the default argument
greet_user("Ameer")  # Will use the provided argument

# 📝 Exercise 6: Function to Find the Maximum of Three Numbers
# Define a function that returns the maximum of three numbers

def find_max(num1, num2, num3):
    return max(num1, num2, num3)

print(f"The maximum number is: {find_max(10, 20, 30)}")
