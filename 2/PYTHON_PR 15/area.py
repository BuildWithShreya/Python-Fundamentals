# area___overloading

class rectcircle:
    def area(self,x,y= None):
        if y is None:
            print("Area of Circle:", 3.14*x*x)
        else:
            print("Area of Rectangle: ",x*y)
rc= rectcircle()
rc.area(12,5)
rc.area(10)