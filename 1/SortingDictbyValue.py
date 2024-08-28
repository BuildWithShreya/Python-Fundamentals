# This Python script sorts a dictionary by value.

# Create a dictionary.
my_dict = {
    "a": 10,
    "b": 5,
    "c": 15,
    "d": 20,
}

# Sort the dictionary by value in ascending order.
sorted_dict_asc = sorted(my_dict.items(), key=lambda x: x[1], reverse=False)

# Sort the dictionary by value in descending order.
sorted_dict_desc = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

# Print the sorted dictionaries.
print("Sorted dictionary in ascending order:", sorted_dict_asc)
print("Sorted dictionary in descending order:", sorted_dict_desc)