# Employee Management System

# Globally a list has been created for employees to add
employees = []


# Add Employee
def add_employee():
    flag = True  # for checking the uniqueness of the ID of the employee
    print("Enter Employee Details:")
    id = int(input("ID: "))
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    position = input("Position: ")
    salary = float(input("Salary: "))
    # Now Checking whether the ID provided by the user already exists or not
    if not employees:
        flag = True
    else:
        for emp in employees:
            if id == emp['id']:
                flag = False
                break
    if flag == True:
        # If ID is unique then add the details

        # Dictionary of employee with his details as key value pair has been added
        employee = {'id': id, 'name': name, 'age': age, 'gender': gender, 'position': position, 'salary': salary}

        # Now this detail is added in that globally declared list.
        employees.append(employee)
        print("Employee added successfully.")
    else:
        print('ID already exists!!')


# Update Employee
def update_employee():
    # Taking ID from the user on which update is to be performed.
    print("Enter Employee ID:")
    id = int(input("ID: "))

    # Loop for finding the employee with the ID provided to update details
    for employee in employees:
        if employee['id'] == id:  # condition for finding the employee
            print('Which Information you want to update : ')
            print('1. Name')
            print('2. Age')
            print('3. Gender')
            print('4. Position')
            print('5. Salary')
            ch = int(input('Enter Your choice : '))

            #
            if ch == 1:
                # showing the current value of column name
                print('Name : ', employee['name'])
                # Taking the new value from the user to update
                employee['name'] = input('Enter the new name :')
            elif ch == 2:
                print('Age : ', employee['age'])
                employee['age'] = input('Enter the age :')
            elif ch == 3:
                print('Gender :', employee['gender'])
                employee['gender'] = input('Enter the Gender : ')
            elif ch == 4:
                print('Name : ', employee['position'])
                employee['position'] = input('Enter the position :')
            elif ch == 5:
                print('Salary : ', employee['salary'])
                employee['salary'] = input('Enter the salary :')
            print('Employee Details updated Successfully')
            print()

            return
    print("Employee not found.")


# Delete Employee
def delete_employee():
    print("Enter Employee ID:")
    id = int(input("ID: "))
    for employee in employees:
        if employee['id'] == id:

            employees.remove(employee)
            print("Employee deleted successfully.")
            return

    print("Employee not found.")


# List Employees
def list_employees():
    if len(employees) == 0:
        print("No employees found.")
        return
    # Printing in tabular format
    print("ID\tName\tAge\tGender\tPosition\tSalary")
    print()
    for employee in employees:
        print(f"{employee['id']}\t{employee['name']}\t{employee['age']}\t{employee['gender']}\
\t{employee['position']}\t{employee['salary']}")