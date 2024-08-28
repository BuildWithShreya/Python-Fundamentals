from StringOp import my_string

my_dict = {'shreya': 2106031, 'Siddhi': 2106033, 'Sneha': 2106032, 'Abhay': 2106029, 'Rishi': 2106039}

print("Length of the dictionary:", len(my_dict))

print("Keys in the dictionary:", my_dict.keys())

print("Values in the dictionary:", my_dict.values())

print("Key-value pairs in the dictionary:", my_dict.items())

key_to_pop = 'shreya'
print("Removed value for key", key_to_pop, ":", my_dict.pop(key_to_pop))

print("Removed last key-value pair:", my_dict.popitem())

my_dict.clear()
print("Cleared dictionary:", my_dict)

new_dict = {'x': 10, 'y': 20}
my_dict.update(new_dict)

print("Updated dictionary:", my_dict)
nd=my_dict+new_dict

print(nd)
key_to_check = 'x'
print("Is key", key_to_check, "present in the dictionary?", key_to_check in my_dict)






















































