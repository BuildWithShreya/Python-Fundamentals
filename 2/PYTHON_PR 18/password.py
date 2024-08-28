# User defined Exception

class IncorrectPasswordError(Exception):
    pass
try:
    password= "gppune"
    user= input("Enter Password:")
    if user!= password:
        raise IncorrectPasswordError("Error: IncorrectPasswordError has occur")
    print("Password is correct")
except IncorrectPasswordError as e:
    print(e)