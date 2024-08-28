# Program to generate random float whare value is between 5 and 50 using built in maths function.

import random
num= 10
random_float= []
for i in range(num):
    random_float.append(random.uniform(5,50))
print(random_float)