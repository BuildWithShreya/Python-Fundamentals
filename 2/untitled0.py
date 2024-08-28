a= [1,6,4,3,8,7]
print(a)

b= (1,6,4,3,8,7)
print(b)

c= {1,6,4,3,8,7}
print(c)

c.remove(6);
print(c)

c.pop()          # remove first element....no argument
print(c)

c.discard(8)
print(c)

list1= [1,3,4,2]
x= list1.pop(2)
print(set([x]))
print(list1)
print(x)

set1= {3,4,3,5,1,"sa",87,45,"ra",67}
print(set1)
set1.remove("ra")
print(set1)
set1.remove(3)
print(set1)

y= 10
#x= y+=2   #syntax error
print(x)

a= 7
b= 4
c= 5
print(a&b)
print(a&c)
print(b&c)
print(a|b)
print(a^b)

p= [2,5,3,7]
for val in p:
    pass

print(p[:-2])
print(p[2:])








