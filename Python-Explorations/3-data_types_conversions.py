# Introduction

# In Python, data types have specific purposes and behaviors. Sometimes,
# we need to convert data from one type to another for calculations, comparisons,
# or storing data efficiently. This guide explores different data type
# conversions in Python.

# 1. Built-in Conversion Functions

# Python provides several built-in functions for common conversions:

# - `int(x)`: Converts `x` to an integer. Raises an error if conversion fails.
# - `float(x)`: Converts `x` to a floating-point number. Raises an error if conversion fails.
# - `str(x)`: Converts `x` to a string representation.
# - `bool(x)`: Converts `x` to a boolean value (True or False).

# Example:

num_str = "123"
num_int = int(num_str)  # Convert string to integer
print(f"Original string: {num_str}, Converted integer: {num_int}")  # Output: Original string: 123, Converted integer: 123

# 2. Implicit Conversions

# Python sometimes performs implicit conversions automatically during operations.
# This can be convenient, but be cautious of unexpected behavior:

# - Integer division (`/`) returns a float if the result is not a whole number.
# - Mixing numeric types in operations usually promotes the result to a float.

# Example:

num_int = 10
num_float = 3.14
result = num_int / num_float  # Implicit conversion to float
print(f"Division result: {result}")  # Output: Division result: 3.1746031746031744

# 3. Converting Between Strings and Numbers

# Use `int()`, `float()`, or `complex()` to convert strings to numbers, considering:

# - `int()` accepts optional base (e.g., `int("1010", 2)` for binary).
# - `float()` handles scientific notation (e.g., `"1.23e4"`).
# - `complex()` parses complex numbers (e.g., `"3+4j"`).

# Example:

num_str = "3.14159"
num_float = float(num_str)
print(f"Original string: {num_str}, Converted float: {num_float}")  # Output: Original string: 3.14159, Converted float: 3.14159

# 4. Converting Other Data Types

# Use specific methods or functions for less common conversions:

# - `list(x)`: Creates a list from an iterable (e.g., string, tuple).
# - `tuple(x)`: Creates a tuple from an iterable.
# - `set(x)`: Creates a set from an iterable, removing duplicates.
# - `dict(x)`: Creates a dictionary from an iterable of key-value pairs.

# Example:

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(f"Original list: {my_list}, Converted tuple: {my_tuple}")  # Output: Original list: [1, 2, 3], Converted tuple: (1, 2, 3)

# 5. Error Handling and Considerations

# Not all conversions are possible (e.g., converting "hello" to an integer).
# Always handle potential errors using `try-except` blocks or checking data types beforehand.

# Remember, choosing the appropriate conversion function or method depends on the data and desired outcome.

# By understanding these concepts and using them effectively, you can write more versatile and robust Python code!
