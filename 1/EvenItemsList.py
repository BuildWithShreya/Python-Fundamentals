def select_even_items(lst):
    return [item for item in lst if item % 2 == 0]

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_items = select_even_items(my_list)
print("Even items:", even_items)
