#default parameter
def mul(x=2,y=6,z=9):
    res=x*y*z
    return (res)

print("Multi is :",mul(12,3,6))
print("Multi is :",mul(12,3))
print("Multi is :",mul(12))
print("Multi is :",mul())
print("Multi is :",mul(z=2,y=6,x=7))

#functions returning multiple values
def array(n):
    add = 0
    for x in n:
        add += x
    avg = add / len(n)
    return add, avg

arr = [99, 99, 100, 99, 100]
a, b = array(arr)
print("Addition is:", a)
print("Average is:", b)


#Recursion Factorial
def factt(n):
    if n<=1 :
        return 1
    else :
        return n*factt(n-1)
print("Factorial is : ",factt(5))

#variable length argumnets
def show(*args):
    for a in args:
        print(a)
show(1,2,3)

#lambda
square=lambda x:x*x
print('Square : ',square(2))

#filter
seq = [0, 1, 2, 6, 7, 3, 4, 5]
res_odd = filter(lambda x: x % 2, seq)
print("Odd numbers:", list(res_odd))
res_even = filter(lambda x: x % 2 == 0, seq)
print("Even numbers:", list(res_even))

#Maps
numbers = [1, 2, 3, 4, 5]
strings = ["one", "two", "three", "four", "five"]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared Numbers:", squared_numbers)
uppercase_strings = list(map(lambda s: s.upper(), strings))
print("Uppercase Strings:", uppercase_strings)
