# number of items into dozen and remaining units

items= 497
dozen= int(items / 12)
units= items % 12
print(items," = ",dozen  ,"dozen and ", units,"units")