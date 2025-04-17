# guess_my_number.py
# Author: Ameer Hamza - Age: 21 - GIAIC Student

import random

secret = random.randint(1, 10)
print("Guess a number between 1 and 10")

guess = int(input("Your guess: "))

if guess == secret:
    print("🎉 Congratulations! You guessed it right.")
else:
    print(f"😞 Sorry! The number was {secret}")
