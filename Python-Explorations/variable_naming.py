# # The Foundations:

# # Valid Characters: Your variable names can consist of letters (a-z, A-Z), numbers (0-9), and underscores (_).
# # Start Smart: The first character must be a letter or underscore. No numbers in the lead!
# # Case Matters: age and Age are distinct variables. Choose consistently (lowercase with underscores is common).
# # Reserved Words: Don't use Python keywords like for, if, or def as variable names.
# # Best Practices:

# # Clarity is Key: Use descriptive names that reflect the variable's purpose. customer_name is better than x.
# # Consistency Counts: Stick to a naming convention (e.g., snake_case, camelCase) throughout your code.
# # Avoid Abbreviations: Unless universally understood (num_items), spell things out for readability.
# # Meaningful Prefixes/Suffixes: Use is_ for booleans, total_ for sums, etc.

# # In Python, you can only use a limited set of characters for variable names. Unfortunately, none of the characters you mentioned ($, *, -, and ...) are allowed. Here's what you need to know:

# # Valid Characters:

# # Letters (a-z, A-Z)
# # Numbers (0-9)
# # Underscore (_)
# # Invalid Characters:

# # Any special characters not mentioned above (including $, *, -, and ...)
# # Spaces




# # Examples:

# # Good:

# first_name = "Alice"
# customer_id = 12345
# is_admin = True
# total_price = 0.0
# calculate_area(length, width)  # Function names follow similar rules


# # bad : 
# x = "Name"  # Unclear
# n = 10  # Cryptic
# isAdmin = True  # Inconsistent capitalization
# price = 0  # Missing units
# calcArea(l, w)  # Abbreviated function name

# # These variable names will cause errors
# price$ = 10.99
# discount* = 5
# user-id = 123
# data... = "some_information"

