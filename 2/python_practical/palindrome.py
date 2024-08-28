p= int(input("Enter number:"))
m= p
rev= 0
while(m>0):
    rem= m% 10
    rev= (rev*10)+rem
    m= m//10
if(p==rev):
    print(p,"is palindrome")
else:
    print(p,"is not palindrome")
    