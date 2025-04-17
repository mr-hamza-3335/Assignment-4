# control_flow_console.py
# Author: Ameer Hamza - Age: 21 - GIAIC Student

print("Control Flow for Console Application")

# Example 1: If-Else
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor.")

# Example 2: For Loop
print("Counting from 1 to 5 using a for loop:")
for i in range(1, 6):
    print(i)

# Example 3: While Loop
print("Counting down from 10 using a while loop:")
count = 10
while count > 0:
    print(count)
    count -= 1

print("End of Control Flow Example!")
