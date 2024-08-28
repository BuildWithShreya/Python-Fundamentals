my_tuple = (1, 2, 3, 4, 5)

print("Length of the tuple:", len(my_tuple))

print("Maximum value in the tuple:", max(my_tuple))

print("Minimum value in the tuple:", min(my_tuple))

print("Sum of the elements in the tuple:", sum(my_tuple))

value_to_find = 4
print("Index of", value_to_find, "in the tuple:", my_tuple.index(value_to_find))

list_to_convert = [6, 7, 8]
converted_tuple = tuple(list_to_convert)
print("Converted tuple from list:", converted_tuple)

sorted_tuple = tuple(sorted(my_tuple))
print("Sorted tuple:", sorted_tuple)

