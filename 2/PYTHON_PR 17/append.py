# append hello world

with open("sara.txt",'a') as f:
    f.write("Hello World")
    print("Text appended successfully")
f.close()