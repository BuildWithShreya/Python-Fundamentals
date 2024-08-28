# Given dictionaries
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Combine dictionaries by adding values for common keys
combined_dict = {}

# Loop through keys in d1
for key in d1:
    # Check if the key is present in d2
    if key in d2:
        # Add the values for common keys
        combined_dict[key] = d1[key] + d2[key]
    else:
        # If the key is unique to d1, add its value to the combined dictionary
        combined_dict[key] = d1[key]



# Print the result
print("Combined Dictionary:", combined_dict)
