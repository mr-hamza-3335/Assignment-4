# joke_bot.py
# Author: Ameer Hamza - Age: 21 - GIAIC Student

import random

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "What do you call fake spaghetti? An impasta.",
    "Why was the math book sad? Because it had too many problems.",
    "What do you call cheese that isn't yours? Nacho cheese."
]

print("Welcome to the Joke Bot!")
input("Press Enter to get a random joke...")

joke = random.choice(jokes)
print("😂 Joke:", joke)
