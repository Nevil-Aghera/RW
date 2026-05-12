import datetime


def datetime_operations():

    while True:

        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format current date")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            now = datetime.datetime.now()

            print("\nCurrent Date and Time:", now)

        elif choice == "2":

            d1 = input("Enter first date (YYYY-MM-DD): ")
            d2 = input("Enter second date (YYYY-MM-DD): ")

            date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
            date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")

            diff = abs((date2 - date1).days)

            print("Difference:", diff, "days")

        elif choice == "3":

            now = datetime.datetime.now()

            print(now.strftime("%d-%m-%Y %H:%M:%S"))

        elif choice == "4":
            break

        else:
            print("Invalid Choice")