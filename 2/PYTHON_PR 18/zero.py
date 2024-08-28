# buit-in exception

try:
    num= int(input("Enter numerator:"))
    den= int(input("Enter Denominator:"))
    result= num/den
    print("Result:",result)
    
except ZeroDivisionError:
    print("Error: Division by Zero is not allowed")
    
except ValueError:
    print("Error: Please Enter valid Integer")
    
