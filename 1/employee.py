class Employee:
  def __init__(self, name, department, salary):
    self.name = name
    self.department = department
    self.salary = salary

  def read_info(self):
    self.name = input("Enter employee name: ")
    self.department = input("Enter employee department: ")
    self.salary = float(input("Enter employee salary: "))

  def print_info(self):
    print(f"Employee Name: {self.name}")
    print(f"Department: {self.department}")
    print(f"Salary: ${self.salary:.2f}")  # Format salary with 2 decimal places

# Create an employee object
emp1 = Employee("", "", 0.0)  # Initialize with empty values

# Allow user to enter information
emp1.read_info()

# Print the employee information
emp1.print_info()
