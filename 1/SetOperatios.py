# Create two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8,18,4}

# Display the initial sets
print("Set 1:", set1)
print("Set 2:", set2)

# Intersection of sets
print("Intersection of sets:", set1.intersection(set2))

# Union of sets
print("Union of sets:", set1.union(set2))

# Set difference
print("Set difference (Set 1 - Set 2):", set1.difference(set2))

# Symmetric difference
print("Symmetric difference of sets:", set1.symmetric_difference(set2))

# Clear a set
print("Cleared Set 1:", set1.clear())
