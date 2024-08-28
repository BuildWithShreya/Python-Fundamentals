# Define a sample string
my_string = "hello shreyaaa"

# 1. Length of the string
print("Length of the string:", len(my_string))

# 2. Convert to uppercase
print("Uppercase:", my_string.upper())

# 3. Convert to lowercase
print("Lowercase:", my_string.lower())

# 4. Capitalize the first character
print("Capitalized:", my_string.capitalize())

# 5. Title case
print("Title case:", my_string.title())

# 6. Check if all characters are alphabetic
print("Is alphabetic:", my_string.isalpha())

# 7. Check if all characters are digits
numeric_string = "12345"
print("Is numeric:", numeric_string.isdigit())

# 8. Strip leading and trailing whitespaces
print("Stripped:", my_string.strip())

# 9. Replace substring
new_string = my_string.replace("hello", "ILU")
print("Replace:", new_string)

# 10. Find substring index
index = my_string.find("ILU")
print("Index of 'ILU':", index)

my_string = "apple orange banana"
fruits = my_string.split(',')
print(fruits)

fruits1 = ['apple', 'orange', 'banana']
fruit_string = '*'.join(fruits1)
print(fruit_string)

# Encode a string
text = "Hello, world!"
encoded_text = text.encode('utf-8')
print(encoded_text)  # Output: b'Hello, world!'

# Strip leading and trailing whitespaces
text = "  Hello, world!  "
stripped_text = text.strip()
print(stripped_text)  # Output: Hello, world!

# Strip leading whitespaces
lstripped_text = text.lstrip()
print(lstripped_text)  # Output: Hello, world!

# Strip trailing whitespaces
rstripped_text = text.rstrip()
print(rstripped_text)  # Output:  Hello, world!

# Check if a string starts with a substring
starts_with_hello = text.startswith("Hello")
print(starts_with_hello)  # Output: True

# Check if a string ends with a substring
ends_with_world = text.endswith("world!")
print(ends_with_world)  # Output: True

# Find the first occurrence of a substring
index_of_hello = text.find("Hello")
print(index_of_hello)  # Output: 2

# Find the last occurrence of a substring
rindex_of_hello = text.rfind("Hello")
print(rindex_of_hello)  # Output: 2

# Get the index of a substring (raises ValueError if not found)
index_of_world = text.index("world")
print(index_of_world)  # Output: 7

