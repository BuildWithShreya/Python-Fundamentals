# program to print a tuple

a= (12,34,56,"GPP")
print(a)
b= (56,"sara",a)
print(b)
b[1]= 23                       # 'tuple' object does not support item assignment
print(b[1]) 