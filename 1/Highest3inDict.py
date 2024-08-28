data = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}

# Method 2: Using sorted() and slicing
sorted_values = sorted(data.values(), reverse=True)
top_3_values = sorted_values[:3]
print(top_3_values)  # Output: [500, 400, 300]
