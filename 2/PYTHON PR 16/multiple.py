# multiple inheritance

class emp:
    def __init__(self,salary):
        self.salary= salary
        
class person:
    def __init__(self,name):
        self.name= name
        
class mix(emp,person):
    def __init__(self,salary,name):
        emp.__init__(self,salary)
        person.__init__(self,name)
        
    def show(self):
        print("Salary: ",self.salary)
        print("Name: ",self.name)

salary= int(input("Enter Salary:"))
name= input("Enter Name:")    
    
m1= mix(salary,name)
m1.show()
        
    
    