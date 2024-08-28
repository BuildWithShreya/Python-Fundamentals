class Degree:
  def getDegree(self):
    print("I got a degree")

class Undergraduate(Degree):
  def getDegree(self):
    print("I am an Undergraduate")

class Postgraduate(Degree):
  def getDegree(self):
    print("I am a Postgraduate")

undergrad = Undergraduate()
postgrad = Postgraduate()
degree = Degree()

undergrad.getDegree()  # Output: I am an Undergraduate
postgrad.getDegree()  # Output: I am a Postgraduate
degree.getDegree()    # Output: I got a degree
