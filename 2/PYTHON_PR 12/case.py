# program to accept string and calculate number of lowercase letters and uppercase letters in string

def check(str):
    lower= 0
    upper= 0
    for i in str:
        if(i.islower()):
            lower+= 1
        else:
            upper+= 1
    print("Number of lowercase letters:",lower)
    print("Number of uppercase letters:",upper)
    
str= "GPPune"   
check(str)