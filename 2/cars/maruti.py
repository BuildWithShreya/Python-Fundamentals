# maruti.py

class maruti:
    def __init__(self):
        self.models=['800','Alto','WagonR']
    def pModel(self):
        print("Models of Maruti:")
        for model in self.models:
            print('\t%s'%model)