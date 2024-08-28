row=5
for i in range(row):
    for j in range(i):
        print(i,end=' ')
    print(' ')

print('\n')
row=5
j=1
i=1
for i in range(1,row):
    for j in range(1,i+1):
        print(j,end=' ')
    print(' ')

for i in range(row+1):
    print(" * " * i)



print('\n')

for i in range(1, row + 1):
    print(" " * (row - i) + "* " * i)

print("\n")
for i in range(row,0,-1):
    space=" "*(row-i)
    binary="10"* (i-1)+"1"
    print(space+binary)

def print_diamond(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(1, 2 * i):
            print("*", end="")
        print()

    for i in range(rows - 1, 0, -1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(1, 2 * i):
            print("*", end="")
        print()
rows = 5
print_diamond(rows)
