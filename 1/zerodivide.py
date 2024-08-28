def divide_numbers(x, y):
    try:
        result = x / y
        print(f"Result of division: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Example usage:
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

divide_numbers(numerator, denominator)
