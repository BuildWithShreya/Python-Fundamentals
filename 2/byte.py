# program to print bytes data element

b= [23,45,78,97,54]
m= bytes(b)
print(m[0])
#  m[2]= 89                       # 'bytes' object does not support item assignment
print(m[2])

n= bytearray(b)                   # 'bytearray' supports item assignment
print(n[3])
n[4]= 67
print(n[4])