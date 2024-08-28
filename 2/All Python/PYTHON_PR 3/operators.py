# Program using Arithmetic, Logical and Bitwise Operators

# Arithmetic
a= int(input("Enter first number: "));
b= int(input("Enter second number: "));
c= a+b;
print("Addition:",c);
d= a-b;
print("Subtraction:",d);
m= a*b;
print("multiplication:",m);
n= a/b;
print("Division:",n);
p= a%b;
print("Modulus:",p);
q= a**b;
print("Exponent:",q);
x= a//b;
print("Floor Division:",x);

# Logical
y= (a>b)and(a==b);
print("Logical AND:",y);
z= (a>b)or(a==b);
print("Logical OR:",z);
w= not(a<b);
print("Logical NOT:",w);

# Bitwise
AND= (a & b);
print("Bitwise AND:",AND);
OR= (a | b);
print("Bitwise OR:",OR);
NOT= (~a);
print("Bitwise NOT:",NOT);
XOR= (a^b);
print("Bitwise XOR:",XOR);
RIGHT= (a>>2);
print("Bitwise RIGHT:",RIGHT);
LEFT= (a<<2);
print("Bitwise LEFT:",LEFT);











