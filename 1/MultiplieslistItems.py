def multiply_list(lst):
    result = 1
    for item in lst:
        result *= item
    return result

# Example usage
my_list = [2, 3, 4]
result_multiply = multiply_list(my_list)
print("Product of the list:", result_multiply)
