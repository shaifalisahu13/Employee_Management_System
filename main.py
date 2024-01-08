from new import *
while True:
    # Through this loop the execution of the program starts
    # and this is the user view
    print()
    print("----Employee Management System-----")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. List Employees")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_employee()
    elif choice == 2:
        update_employee()
    elif choice == 3:
        delete_employee()
    elif choice == 4:
        list_employees()
    elif choice == 5:
        print('Program Exited!!')
        break
    else:
        print("Invalid choice. Please try again.")

