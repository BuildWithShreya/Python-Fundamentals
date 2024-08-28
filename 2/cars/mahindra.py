# mahindra.py

class mahindra:
    def __init__(self):
        self.models= ['Scorpio','Bolero','Xylo']
    def PModels(self):
        print("Models of Mahindra:")
        for model in self.models:
            print('\t%s'%model)