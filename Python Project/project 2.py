print("Welcome to the Interactive Personal Data Collector! ")

print()

print("Select an option:")
print("1. Generate a Pattern")
print("2. Analyze a Range of Numbers")
print("3. Exit")

choice = input ("enter choice num :")

if choice == '1':
    print("Pattern")
    for i in range (1,6):
         for j in range (i):
             print("*",end="")
         print()
elif choice == '2':
    start = int (input("enter the starting num: "))
    end = int(input("Enter the end of range: "))
    total = 0 
    for i in range(start, end + 1):
        total += i

        if i % 2 == 0:
            print(i,"is even")
        else:
             print(i,"is odd")
        
    print("Sum of elements from", start, "to", end, "is:", total)
          
elif choice == '3':
    print("exiting the program. goodbye!")