print("welcome to the data analyzer and transfromer program")

data = []

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

while True:
    print("\nMenu:")
    print("1. input data")
    print("2. display data summary")
    print("3. calculate factorial")
    print("4. filter data by threshold")
    print("5. sort data")
    print("6. display dataset statistics")
    print("7. exit pro")

    choice = input("Please enter your choice: ")

    if choice == '1':
        string = input("Enter data for a 1D array (separated by spaces): ")
        data = list(map(int, string.split()))
        print("Data has been stored successfully!")

    elif choice == '2':
        if not data:
            print("No data available. Please input data first.")
            continue
        print("\nData Summary:")
        print("Total elements:", len(data))
        print("Minimum value:", min(data))
        print("Maximum value:", max(data))
        print("Sum of all values:", sum(data))
        print("Average value:", sum(data) / len(data))

    elif choice == '3':
        num = int(input("Enter a number to calculate its factorial: "))
        print("Factorial of", num, "is", factorial(num))

    elif choice == '4':
        if not data:
            print("No data available. Please input data first.")
            continue
        threshold = int(input("Enter a threshold value: "))
        filtered = list(filter(lambda x: x > threshold, data))
        print("Filtered Data:", filtered)

    elif choice == '5':
        if not data:
            print("No data available. Please input data first.")
            continue
        print("1. Ascending")
        print("2. Descending")
        opt = input("Enter your choice: ")
        if opt == '1':
            print("Sorted Data in Ascending Order:", sorted(data))
        elif opt == '2':
            print("Sorted Data in Descending Order:", sorted(data, reverse=True))
        else:
            print("Invalid sorting option!")

    elif choice == '6':
        if not data:
            print("No data available. Please input data first.")
            continue
        min_val = min(data)
        max_val = max(data)
        total_sum = sum(data)
        avg = total_sum / len(data)
        print("Dataset Statistics:")
        print("Minimum Value:", min_val)
        print("Maximum Value:", max_val)
        print("Sum of all values:", total_sum)
        print("Average value:", avg)

    elif choice == '7':
        print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 7.")
