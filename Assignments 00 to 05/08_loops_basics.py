# 📝 Exercise 1: Print Numbers 1 to 10
# Use a for loop to print numbers from 1 to 10

print("Numbers from 1 to 10 using for loop:")
for i in range(1, 11):
    print(i)

# 📝 Exercise 2: Sum of Numbers 1 to N
# Ask user for a number N, and print the sum of numbers from 1 to N

N = int(input("Enter a number: "))
sum_numbers = 0
for i in range(1, N+1):
    sum_numbers += i
print(f"Sum of numbers from 1 to {N} is {sum_numbers}.")

# 📝 Exercise 3: Print Multiples of 7
# Use a while loop to print the first 10 multiples of 7

count = 1
while count <= 10:
    print(7 * count)
    count += 1

# 📝 Exercise 4: Reverse Order Print
# Use a for loop to print numbers from 10 down to 1

print("Numbers from 10 to 1:")
for i in range(10, 0, -1):
    print(i)

# 📝 Exercise 5: Factorial of a Number
# Use a while loop to calculate the factorial of a number

number = int(input("Enter a number to find its factorial: "))
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print(f"Factorial is: {factorial}")

# 📝 Exercise 6: Even Numbers using While Loop
# Print all even numbers between 1 and 50 using while loop

num = 2
print("Even numbers between 1 and 50:")
while num <= 50:
    print(num)
    num += 2
