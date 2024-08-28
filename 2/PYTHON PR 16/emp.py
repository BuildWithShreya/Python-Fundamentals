# inheritance

class employee:
    def __init__(self,name,dept,salary):
        self.name= name
        self.dept= dept
        self.salary= salary
        
    def read(self):
        print("Name:",self.name)
        print("Dept:",self.dept)
        print("Salary:",self.salary)
        
name= input("Enter name:")
dept= input("Enter department:")
salary= int(input("Enter Salary:"))

emp= employee(name,dept,salary)
emp.read()