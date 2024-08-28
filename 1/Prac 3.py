a=2
b=5
print("Arithematic Operators :")
print("Addition\t\t",a+b)
print("Subtraction\t\t",a-b)
print("Multilplication\t",a*b)
print("Division\t\t",a/b)
print("Exponential\t\t",a**b)
print("Modulus\t\t\t",a%b)
print("Floor Division\t",a//b)

print("\nLogical Operators :")
print((a>b)and(a<b))
print((a>b)or(a<b))
print(not(a<b))

print("\nBitwise Operators :")
print("1's Complement\t",~a)#1's complemet
print("bitwise and\t\t",a&b)#bitwise and
print("bitwise or\t\t",a|b)#bitwise or
print("bitwise not\t\t",a^b)#bitwise XoR
print("Left Shift\t\t",a<<b)
print("Right Shift\t\t",a>>b)

print("\nIdentity Operators :")
print("Address of a :",id(a))
print("Address of b :",id(b))
if(a is b):
    print("Same addresses of a and b")
else:
    print("No same addresses of a and b")
y=25
x=25
print("Address of x :",id(x))
print("Address of y :",id(y))
if(x is y):
    print("Same addresses of x and y")
else:
    print("No same addresses of x and y")

print("\nMembership Operators :")
myArr=[10,50,31,33,32]
srch=31
print("in \t\t",srch in myArr)
print("not in\t",srch not in myArr)