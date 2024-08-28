a= 0
b= 1
fib= 0
for i in range(10):
    print(fib,end=" ")
    fib= a+b
    a= b
    b= fib
    