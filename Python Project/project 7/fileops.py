def file_operations():

    while True:

        print("\nFile Operations:")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            filename = input("Enter file name: ")

            file = open(filename, "w")

            file.close()

            print("File Created")

        elif choice == "2":

            filename = input("Enter file name: ")

            data = input("Enter data: ")

            file = open(filename, "w")

            file.write(data)

            file.close()

            print("Data Written")

        elif choice == "3":

            filename = input("Enter file name: ")

            file = open(filename, "r")

            content = file.read()

            file.close()

            print("\nFile Content:")
            print(content)

        elif choice == "4":

            filename = input("Enter file name: ")

            data = input("Enter data: ")

            file = open(filename, "a")

            file.write(data)

            file.close()

            print("Data Appended")

        elif choice == "5":
            break

        else:
            print("Invalid Choice")