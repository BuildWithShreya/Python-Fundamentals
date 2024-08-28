for i in range(5):
    if i == 3:
        pass  # Do nothing for i=3
    else:
        print(i)

print('\ne')

for i in range(5):
    if i%2 == 0:
        continue  # Skip the rest of the loop for i=2
    print(i)

print('\ne')

for i in range(5):
    if i % 2 == 0:
        break  # Exit the loop when i=3
    print(i)
