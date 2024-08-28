dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Creating a new dictionary and concatenating the given dictionaries
concatenated_dict = {}
concatenated_dict.update(dic1)
concatenated_dict.update(dic2)
concatenated_dict.update(dic3)

# Print the result
print("Concatenated Dictionary:", concatenated_dict)
