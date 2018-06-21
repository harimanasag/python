class Employee:
    employeeCount = 0
    def __init__(self, empdictionary):
        self.emp_dictionary = empdictionary
        self.employeeCount = len(empdictionary)
        self.display_employee_details()

    def display_employee_details(self):
        print("Total no of Employees", self.employeeCount)
        employeeSalary = 0
        for count in range(len(self.emp_dictionary)):
            if count <= len(self.emp_dictionary):
                employeeSalary = employeeSalary + float(self.emp_dictionary.get(count)[2])
                print("Employee %s Details :" % str(count+1))
                print("Employee Name: %s, Employee Family: %s, Employee Salary: %f, Employee Department: %s "
                      % (str(self.emp_dictionary.get(count)[0]), str(self.emp_dictionary.get(count)[1]),
                         float(self.emp_dictionary.get(count)[2]), str(self.emp_dictionary.get(count)[3])))
        print("Employees Average Salary:", employeeSalary/self.employeeCount)


class FullTimeEmployee(Employee):
	
    def __init__(self, empdictionary):
        Employee.__init__(self, empdictionary)


validation = "yes"
employeeDictionary = {}
empId = 0
while validation[0] == 'y':
    print("Enter the following information to get employee count and average salary")
    employeeName = input("Enter Employee Name: ")
    employeeFamily = input("Enter Employee Family Name: ")
    employeeSalary = input("Enter Employee Salary Amount: ")
    employeeDepartment = input("Enter Employee Department Name: ")
    if employeeName not in employeeDictionary:
        employeeDictionary[empId] = [employeeName, employeeFamily, employeeSalary, employeeDepartment]
        empId += 1
    else:
        print("Employee %s already exists, Please try again" % employeeName)
    validation = input("Do you want enter more details (yes / no)? ")

Employee(employeeDictionary)
