# python functions that accept string and calculate number of upper cases and lower cases in a string.

str= "GPPune"
lower= 0
upper= 0
for i in str:
    if(i.islower()):
        lower+= 1
    else:
        upper+= 1
print("Number of Lower case letters:",lower)
print("Number of upper case letters:",upper)