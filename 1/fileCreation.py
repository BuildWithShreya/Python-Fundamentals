file_path = "hello.txt"

# Writing to the file
with open(file_path, 'w') as file:
    file.write("Hello, World!")

print(f"Contents written to {file_path}")
