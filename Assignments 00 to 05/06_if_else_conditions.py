# 📝 Exercise 1: Voting Eligibility
# Check if a person is eligible to vote or not (Age >= 18)

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not eligible to vote yet.")

# 📝 Exercise 2: Grade Checker
# Input marks and determine the grade (A, B, C, D, F)

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F")

# 📝 Exercise 3: Find the maximum number
# Take two numbers from the user and find the greater one

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"The greater number is {num1}.")
elif num2 > num1:
    print(f"The greater number is {num2}.")
else:
    print("Both numbers are equal.")

# 📝 Exercise 4: Even or Odd
# Ask the user for a number and check if it's even or odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("It's an even number.")
else:
    print("It's an odd number.")

# 📝 Exercise 5: Temperature Check
# Ask the user for a temperature and determine if it's hot, warm, or cold

temperature = int(input("Enter the temperature: "))

if temperature >= 30:
    print("It's hot!")
elif temperature >= 20:
    print("It's warm!")
else:
    print("It's cold!")
