file_path = "sample.txt"  # Replace with the actual file path

try:
    with open(file_path, 'r') as file:
        content = file.read()
        count_of_a = content.count('a')

        print(f"Number of occurrences of 'a' in {file_path}: {count_of_a}")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")

