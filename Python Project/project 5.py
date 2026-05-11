class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("\nPerson Details")
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):

    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)

        self.emp_id = emp_id
        self.salary = salary

    def show_details(self):
        print("\nEmployee Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


class Manager(Employee):

    def __init__(self, name, age, emp_id, salary, department):
        super().__init__(name, age, emp_id, salary)

        self.department = department

    def show_details(self):
        print("\nManager Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)
        print("Department:", self.department)


person = None
employee = None
manager = None

while True:

    print("\n--- Employee Management System ---")

    print("1. Create Person")
    print("2. Create Employee")
    print("3. Create Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        age = input("Enter Age: ")

        person = Person(name, age)

        print("\nPerson created successfully!")

    elif choice == "2":

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        emp_id = input("Enter Employee ID: ")
        salary = input("Enter Salary: ")

        employee = Employee(name, age, emp_id, salary)

        print("\nEmployee created successfully!")

    elif choice == "3":

        name = input("Enter Name: ")
        age = input("Enter Age: ")
        emp_id = input("Enter Employee ID: ")
        salary = input("Enter Salary: ")
        department = input("Enter Department: ")

        manager = Manager(name, age, emp_id, salary, department)

        print("\nManager created successfully!")

    elif choice == "4":

        print("\n1. Person")
        print("2. Employee")
        print("3. Manager")

        detail = input("\nEnter your choice: ")

        if detail == "1":

            if person:
                person.show_details()
            else:
                print("No Person Created")

        elif detail == "2":

            if employee:
                employee.show_details()
            else:
                print("No Employee Created")

        elif detail == "3":

            if manager:
                manager.show_details()
            else:
                print("No Manager Created")

        else:
            print("Invalid Choice")

    elif choice == "5":

        print("\nGoodbye!")
        break

    else:
        print("\nInvalid Choice")