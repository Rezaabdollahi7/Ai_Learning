# Data Types in Python

# Numeric Types
# Integers (whole numbers)
num_int = 10
print(type(num_int))  # Output: <class 'int'>

# Floating-point numbers (decimals)
num_float = 3.14
print(type(num_float))  # Output: <class 'float'>

# Complex numbers (real and imaginary parts)
num_complex = 3 + 4j
print(type(num_complex))  # Output: <class 'complex'>

# Sequence Types
# Ordered collections of items
# Lists (mutable)
my_list = [1, "hello", True]
print(type(my_list))  # Output: <class 'list'>
my_list[0] = 5  # Modify list element
print(my_list)  # Output: [5, "hello", True]

# Tuples (immutable)
my_tuple = (10, "world", False)
print(type(my_tuple))  # Output: <class 'tuple'>
# my_tuple[0] = 20  # Error: tuples are immutable

# Range (immutable sequence of numbers)
num_range = range(5)  # Generates numbers 0 to 4
print(type(num_range))  # Output: <class 'range'>
print(list(num_range))  # Convert to list for printing: [0, 1, 2, 3, 4]

# Strings (sequence of characters)
my_string = "This is a string"
print(type(my_string))  # Output: <class 'str'>
# my_string[0] = 'T'  # Error: strings are immutable

# Mapping Types
# Dictionaries (unordered collection of key-value pairs)
my_dict = {"name": "Alice", "age": 30}
print(type(my_dict))  # Output: <class 'dict'>
my_dict["age"] = 31  # Modify dictionary value
print(my_dict)  # Output: {'name': 'Alice', 'age': 31}

# Set Types
# Unordered collections of unique elements
my_set = {1, 2, 3, 2}  # Duplicates are removed
print(type(my_set))  # Output: <class 'set'>
# my_set.add(4)  # Add element to set
# print(my_set)  # Output: {1, 2, 3, 4}

# Frozenset (immutable version of set)
my_frozenset = frozenset({10, "hello"})
print(type(my_frozenset))  # Output: <class 'frozenset'>
# my_frozenset.add("world")  # Error: frozensets are immutable

# Boolean Type
my_bool = True
print(type(my_bool))  # Output: <class 'bool'>

# None Type (represents absence of a value)
my_none = None
print(type(my_none))  # Output: <class 'NoneType'>

# Remember, understanding data types is crucial for writing efficient and readable Python code!
