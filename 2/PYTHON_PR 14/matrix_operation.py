# program to create two matrices and perform addition, subtraction, multiplication and division operation on matrix

import numpy as np

A= np.array([[1,2],[3,4]])
B= np.array([[4,5],[6,7]])

print("Elements of First Matrix: ")
print(A)

print("Elements of Second Matrix: ")
print(B)

print("Addition of Two Matrices")
print(np.add(A,B))

print("Subtraction of Two Matrices")
print(np.subtract(A,B))

print("Multiplication of Two Matrices")
print(np.multiply(A,B))

print("Division of Two Matrices")
print(np.divide(A,B))