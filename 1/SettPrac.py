my_set = {3, 6, 9, 12, 15}

print("Initial Set:", my_set)

my_set.add(18)
my_set.update([12, 24, 27])

print("Set after adding members:", my_set)

item_to_remove = 12
my_set.remove(item_to_remove)

print("Set after removing", item_to_remove, ":", my_set)
