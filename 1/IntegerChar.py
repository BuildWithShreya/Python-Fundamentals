class IntegerCharPrinter:
    @staticmethod
    def print_int_char(n, c):
        print(f"Integer: {n}, Character: {c}")

    @staticmethod
    def print_char_int(c, n):
        print(f"Character: {c}, Integer: {n}")

# Example usage:
# Calling the first method
IntegerCharPrinter.print_int_char(5, 'A')

# Calling the second method
IntegerCharPrinter.print_char_int('B', 10)
