x=1
while True:
    if (x%5)== 0:
        break;
    print(x)
    x+= 1
    
a= [1,2,3,4,5]

del a[2]
print(a)

a.remove(4)
print(a)

a.pop(0)
print(a)
print([1,2,3]+[4,5])

b=(12,3)
c=(1,4)
print(b+c)
print(b[1])
print(len(c))

s={1,2,2,3,4,5}
print(s)

s.remove(2)
print(s)

s.pop()
print(s)

s.add(7)
print(s)

z= {1:'sa',2:'va',3:'da'}
del z[2]
print(z)
z.pop(1)
print(z)

print(z.keys())

p= [[0],[1]]
print((''.join(list(map(str,p))),))

print(2**(3**2))
print((2**3)**2)
print(2**3**2)

i= 1
while True:
    if i%3== 0:
        break
    print(i)
    i+= 1
    
y= 'sa'
w= 'ra'
print(y+w)


print(3*1**3)

m= 23.4
print(int(m))

str= "hell0"
print(str[:2])

print(round(45.8))

def sample(a):
    a= a+'2'
    a= a*2
    return a
print(sample("hello"));

print('"sara"sa')
print("'sara'")
print("gp,'pune'")
# print('3\')           syntaxerror

print('tom\ndick\nharry')
print((80+90)/2)
print('hello-'+'how-are-you')

print(0.1+0.2== 0.3)

print(~~~~~~5)

print(float('56'+'78'))
# print(float('56+78'))     #ValueError: could not convert string to float

print(round(0.5)-round(-0.5))
print(round(0.5))
print(round(-0.5))

print(3^4)

l= [3,2,6,5]
print(l[:-2])
















