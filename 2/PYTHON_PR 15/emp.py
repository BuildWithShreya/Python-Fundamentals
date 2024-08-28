# Method Overriding

class employee:
    def message(self):
        print("This message is from Employee class")
class department(employee):
    def message(self):
        print("This message is from department class which inherit employee class")
emp= employee()
dept= department()
emp.message()
print("------------------------------------------------")
dept.message()