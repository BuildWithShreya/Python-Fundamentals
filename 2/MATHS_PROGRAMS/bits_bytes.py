# Program to convert bits to megabytes, gigabytes and terabytes.
bit= int(input("Enter number of bits:"));
megabytes= (bit/1000000);
gigabytes= (bit/8000000000);
terabytes= (bit/8000000000000);
print(bit,"bit=",megabytes,"megabytes");
print(bit,"bit=",gigabytes,"gigabytes");
print(bit,"bit=",terabytes,"terabytes");



bit= int(input("Enter no.of bits: "))
mb= bit/1000000
gb= bit/8000000000
tb= bit/8000000000000
print(bit,"bit= ",mb,"megabytes")
print(bit,"bit= ",gb,"gigabytes")
print(bit,"bit= ",tb,"terabytes")