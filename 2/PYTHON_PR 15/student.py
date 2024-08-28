# Method Overloading

class student:
    def hello(self,name= None):
        if name is not None:
            print("Hey",name)
        else:
            print("Hey")
stud= student()
stud.hello()
stud.hello("Sara")