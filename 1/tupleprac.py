flower_tuple = ("Rose", "Tulip", "Lily", "Sunflower", "Daisy","Tulip")

print("Original tuple:", flower_tuple)
print("Element at index 2:", flower_tuple[2])

index_of_lily = flower_tuple.index("Lily")
print("Index of 'Lily':", index_of_lily)

count_of_tulip = flower_tuple.count("Tulip")
print("Count of 'Tulip':", count_of_tulip)

tuple_length = len(flower_tuple)
print("Length of the tuple:", tuple_length)

is_present = "Sunflower" in flower_tuple
print("Is 'Sunflower' present in the tuple?", is_present)
