data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

# Method 1: Using a set to store unique values
unique_values = set()
for item in data:
    for value in item.values():
        unique_values.add(value)

print(unique_values)  # Output: {'S001', 'S009', 'S005', 'S002', 'S007'}
