# Program to find area and circumference of circle using inbuilt math module
import math
radius= float(input("Enter radius:"))
area= math.pi*radius**2
circum= 2*math.pi*radius
print("Area of circle is",area)
print("Circumference of circle is",circum)