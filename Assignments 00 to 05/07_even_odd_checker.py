# 📝 Exercise 1: Check Even or Odd
# Ask user for a number and check if it's even or odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# 📝 Exercise 2: Print Even Numbers from 1 to 20
# Use loop to print all even numbers between 1 and 20

print("Even numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 📝 Exercise 3: Count Even and Odd Numbers in a List
# Count how many even and odd numbers there are in a list

numbers = [3, 12, 7, 20, 25, 30, 18]
even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")

# 📝 Exercise 4: Number Guessing Game
# The program will generate a random number between 1-100, user has to guess it

import random

random_number = random.randint(1, 100)
guess = None

print("Welcome to the Number Guessing Game!")
while guess != random_number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")

# 📝 Exercise 5: Multiples of 3 and 5
# Print numbers from 1 to 30 which are multiples of both 3 and 5

print("Numbers that are multiples of both 3 and 5:")
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
