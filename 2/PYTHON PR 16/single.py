# single inheritance

class student:
    def __init__(self,name,roll,marks):
        self.name= name
        self.roll= roll
        self.marks= marks

class show(student):    
    def read(self):
        print("Name:",self.name)
        print("Roll No.:",self.roll)
        print("Marks:",self.marks)
        
name= input("Enter name:")
roll= int(input("Enter Roll No:"))
marks= int(input("Enter Marks:"))

stud= student(name,roll,marks)
s1= show(name, roll, marks)
s1.read()  