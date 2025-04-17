# 📝 Exercise 1: Celsius to Fahrenheit Converter
# Formula: (Celsius * 9/5) + 32 = Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

# 📝 Exercise 2: Fahrenheit to Celsius Converter
# Formula: (Fahrenheit - 32) * 5/9 = Celsius

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is equal to {celsius}°C")

# 📝 Exercise 3: Convert Kelvin to Celsius
# Formula: Celsius = Kelvin - 273.15

kelvin = float(input("Enter temperature in Kelvin: "))
celsius = kelvin - 273.15
print(f"{kelvin}K is equal to {celsius}°C")

# 📝 Exercise 4: Check if temperature is above or below freezing point
temp = float(input("Enter a temperature: "))
if temp < 0:
    print("It's freezing!")
else:
    print("It's not freezing.")

# 📝 Exercise 5: Convert a range of Celsius temperatures to Fahrenheit
# Print Celsius and its equivalent Fahrenheit for 0 to 100°C in increments of 10°C

for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit}°F")
