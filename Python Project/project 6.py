from datetime import datetime


def add_entry():
    with open("demo.txt", "a") as file:
        entry = input("write your entry:\n")
        file.write(f"{entry}\n")
    print("\n Entry added successfully!")

def view_entries():
    try:
        with open("demo.txt", "r") as file:
            entries = file.readlines()

        if entries:
            print("\nYour Entries:\n")
            timestamp = datetime.now()
            print(f"---{timestamp.strftime('%Y-%m-%d %H:%M:%S')}---")
            for entry in entries:
                print(f"{entry.strip()}")
        else:
            print("No entries found.\n")

    except FileNotFoundError:
        print("No entries found.\n")

def search_entries():
    keyword = input("Enter keyword to search for: ").lower()
    found = False
    
    try:
        with open("demo.txt", "r") as file:
            print(f"\n--- Search Results for '{keyword}' ---")
            for line in file:
                if keyword in line.lower():
                    print(line.strip())
                    found = True
            if not found:
                print("No entries containing that keyword were found.")
    except FileNotFoundError:
        print("\nNo entries to search.")

def delete_entry():
    try:
        with open("demo.txt", "w") as file:
         print("All entries deleted successfully.")
    except FileNotFoundError:
        print("No entries found. The file does not exist.")

obj = None
print("\nWelcome to Personal Journal Manager!")
while True:
    print("\nPlease select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice = input("\nPlease select an option (1-5): ")

    if choice == '1':
        print("\n--- Add a New Entry ---")
        add_entry() 

    elif choice == '2':
        print("\n--- View All Entries ---")
        view_entries() 

    elif choice == '3':
        print("\n--- Search for an Entry ---")
        search_entries()

    elif choice == '4':
        print("\n--- Delete All Entries ---")
        delete_entry() 

    elif choice == '5':
        print("\n exit")
        break

