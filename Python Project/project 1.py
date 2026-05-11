print("Welcome to the Interactive Personal Data Collector! ")

print()

name=input("Please enter your name: ")
age=int(input("Please enter your age: "))
height=float(input("Please enter your height (in meters): "))
num=int(input("Please enter your favorite number: "))

print()

print("Name:", name, (type (name)), "memory adress:",id(name))
print("Age:", age, (type (age)),"memory adress:",id(age))
print("Height", height, (type(height)),"memory adress:",id(height))
print("Favorite Number:", num, (type (num)), "memory adress:",id(num))

print()

print("Your birth year is approximately: ", 2025-age, "(based on your age.)",age)
print()
print("Thank you for using the Interactive Personal Data Collector. Goodbye!")