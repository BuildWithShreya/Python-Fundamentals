input_file_path = "input.txt"
output_file_path = "output.txt"

# Reading the content from the input file and replacing 'h' with 'a'
with open(input_file_path, 'r') as input_file:
    content = input_file.read()
    modified_content = content.replace('h', 'a')

# Writing the modified content to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(modified_content)

print(f"File '{output_file_path}' created with replaced content.")
