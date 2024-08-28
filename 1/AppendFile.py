file_path = "hello.txt"

# Appending to the file
with open(file_path, 'a') as file:
    file.write("\nHello, World!")

print(f"Appended 'Hello, World!' to {file_path}")

# Reading and printing the contents
with open(file_path, 'r') as file:
    contents = file.read()
    print("File Contents:")
    print(contents)
