# Program to calculate square root of the number.
number= int(input("Enter a number:"));
sqrt= number**0.5;
print("Square Root of",number,"is",sqrt);

#Program to calculate area of Rectangle
length= float(input("Enter Length:"));
breadth= float(input("Enter Breadth:"));
area= length* breadth;
print("Area of Rectangle is",area);

# Program to calculate area and perimeter of square.
side= float(input("Enter side:"));
perimeter= (4*side);
area= (side**2);
print("perimeter of square=",perimeter);
print("area of square=",area);

# Program to swap two variables
a= int(input("Enter first number:"));
b= int(input("Enter second number:"));
print("values before swapping: ");
print("a=",a,"b=",b);
c= a;
a= b;
b= c;
print("values after swapping: ");
print("a=",a,"b=",b);

# Program to calculate volume and surface area of cylinder.
radius= float(input("Enter the Radius:"));
height= float(input("Enter the Height:"));
volume= 3.14*radius*radius*height;       #pi*r*r*h
surface= (2*3.14*radius*radius) + (2*3.14*radius*height);   
print("Volume of Cylinder=",volume);
print("Surface Area of Cylinder=",surface);





