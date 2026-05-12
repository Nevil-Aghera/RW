import random


def random_data_generation():

    while True:

        print("\nRandom Data Generation:")
        print("1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. OTP")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            print("Random Number:",
                  random.randint(1, 100))

        elif choice == "2":

            lst = []

            for i in range(5):
                lst.append(random.randint(1, 50))

            print("Random List:", lst)

        elif choice == "3":

            length = int(input("Enter password length: "))

            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$"

            password = ""

            for i in range(length):
                password += random.choice(chars)

            print("Password:", password)

        elif choice == "4":

            print("OTP:",
                  random.randint(1000, 9999))

        elif choice == "5":
            break

        else:
            print("Invalid Choice")