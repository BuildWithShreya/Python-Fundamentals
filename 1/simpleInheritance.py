class Person:
  def __init__(self, name):
    self.name = name

class Student(Person):
  def __init__(self, name, roll_number, marks):
    super().__init__(name)  # Call base class constructor
    self.roll_number = roll_number
    self.marks = marks

  def read_info(self):
    self.name = input("Enter student name: ")
    self.roll_number = int(input("Enter roll number: "))
    self.marks = float(input("Enter marks: "))

  def print_info(self):
    print(f"Student Name: {self.name}")
    print(f"Roll Number: {self.roll_number}")
    print(f"Marks: {self.marks}")

student1 = Student("", 0, 0.0)
student1.read_info()
student1.print_info()
