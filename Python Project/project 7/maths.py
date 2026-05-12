import math


def mathematical_operations():

    while True:

        print("\nMathematical Operations:")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometry")
        print("4. Circle Area")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            n = int(input("Enter number: "))

            print("Factorial:", math.factorial(n))

        elif choice == "2":

            p = float(input("Enter principal: "))
            r = float(input("Enter rate: "))
            t = float(input("Enter time: "))

            ci = p * ((1 + r / 100) ** t)

            print("Compound Interest:", round(ci, 2))

        elif choice == "3":

            angle = float(input("Enter angle: "))

            print("Sin:", math.sin(math.radians(angle)))
            print("Cos:", math.cos(math.radians(angle)))
            print("Tan:", math.tan(math.radians(angle)))

        elif choice == "4":

            radius = float(input("Enter radius: "))

            area = math.pi * radius * radius

            print("Area of Circle:", round(area, 2))

        elif choice == "5":
            break

        else:
            print("Invalid Choice")