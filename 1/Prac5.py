print("For Loop :")
#Program to Print the characters of String
print("Program to Print the characters of String")
str=(input('Enter a string '))
for i in range(len(str)):
    print(str[i], end='\n')

#Program to find the factorial of a number.
print("Program to find the factorial of a number")
n=int(input('Enter a Number : '))
fact=1
for i in range (1,n+1):
    fact=fact*i
    print(fact)
print('Factorial of ',n,' is : ',fact)

print("")
print("")
print("")