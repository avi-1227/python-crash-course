# Using Variables in Strings
''' In some situations, you'll want to use a variable's value inside a string'''

first_name = "Rohit"
last_name = "Kumar"
full_name = f"{first_name} {last_name}"
print(full_name)
''' You can do a lot with f-strings'''
message = f"Hello, {full_name.upper()}, nice to meet you!"
print(message)

# Stripping Whitespace
# rstrip() - Remove extra whitespace from right side
# lstrip() - Remove extra whitespace from left side 
# strip() - Remove extra whitespace from both side


