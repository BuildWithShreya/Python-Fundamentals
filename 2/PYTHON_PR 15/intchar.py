# intchar ____overloading

class replace:
    def intchar(self,n,c):
        print("Integer",n)
        print("Character",c)
    def intchar(self,c,n):
        print("Character",c)
        print("Integer",n)
rep= replace()
rep.intchar('S',67)
rep.intchar('N',54)
