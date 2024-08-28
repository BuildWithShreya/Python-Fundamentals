# Create a tuple
my_tuple = (10, 20, 30, 20, 40, 10, 50, 30)

# Find repeated items in the tuple
repeated_items = set()
unique_items = set()

for item in my_tuple:
    if item in unique_items:
        repeated_items.add(item)
    else:
        unique_items.add(item)

# Display the result
print("Tuple:", my_tuple)
print("Repeated items:", repeated_items)
