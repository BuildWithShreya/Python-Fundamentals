# degree__overriding

class degree:
    def getDegree(self):
        print("I got a degree")
class undergraduate(degree):
    def getDegree(self):
        print("I am UnderGraduate")
class postgraduate(degree):
    def getDegree(self):
        print("I am PostGraduate")

d1= degree()
d1.getDegree()
d2= undergraduate()
d2.getDegree()
d3= postgraduate()
d3.getDegree()
