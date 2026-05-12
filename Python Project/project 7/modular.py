import uuid

from d1 import datetime_operations
from maths import mathematical_operations
from rdg import random_data_generation
from fileops import file_operations


def generate_uuid():

    print("\nGenerated UUID:")
    print(uuid.uuid4())


def explore_module():

    module_name = input("\nEnter module name: ")

    module = __import__(module_name)

    print(dir(module))


while True:

    print("\n======================")
    print("Multi-Utility Toolkit")
    print("======================")

    print("1. Datetime Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate UUID")
    print("5. File Operations")
    print("6. Explore Module")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        datetime_operations()

    elif choice == "2":
        mathematical_operations()

    elif choice == "3":
        random_data_generation()

    elif choice == "4":
        generate_uuid()

    elif choice == "5":
        file_operations()

    elif choice == "6":
        explore_module()

    elif choice == "7":

        print("\nThank you for using Multi-Utility Toolkit!")

        break

    else:
        print("Invalid Choice")