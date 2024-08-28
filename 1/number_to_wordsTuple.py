def number_to_words(number):
    # Define a tuple with word representations of digits
    words_tuple = ("Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")

    # Convert the number to a string to iterate through each digit
    number_str = str(number)

    # Create a list to store the word representations of digits
    words_list = [words_tuple[int(digit)] for digit in number_str]

    # Join the words into a string
    result = " ".join(words_list)

    return result

# Example usage
example_number = 1234
result_words = number_to_words(example_number)

print(f"{example_number} => {result_words}")
