fruits = ["apple", "banana", "orange", "grape", "kiwi"]
flowers=["Rose", "Tulip", "Lily", "Sunflower", "Daisy","Tulip"]
print("Original list:", fruits)
print("Element at index 2:", fruits[2])

fruits[1] = "pineapple"
print("Modified list:", fruits)

fruits.append("watermelon")
print("List after appending 'watermelon':", fruits)

fruits.remove("orange")
print("List after removing 'orange':", fruits)

fruits.sort()
print("Sorted list:", fruits)

fruits.reverse()
print("Reversed list:", fruits)

fruits.pop(2)
print("Popped list:", fruits)

list_length = len(fruits)
print("Length of the list:", list_length)

print("Slicing of the list:", fruits[2:4])

print("Repetition of the list:", fruits*3)

is_present = "grape" in fruits
print("Is 'grape' present in the list?", is_present)

