# replace

f= open("gpp.txt",'r')
content= f.read()
modified= content.replace('h','a')
f.close()

f= open("gppune.txt",'w')
f.write(modified)
print("Contents copied and replace successfully")
f.close()
