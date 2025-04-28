# Underscores in Numbers
''' When you're writing long numbers, you can group digits using underscores to make large numbers more readable:'''
universe_age = 14_000_000_000
# When you print a number that was defined unsing underscores, Python prints only the digits. Python ignores the underscores when storing these kinds of values.
print(universe_age) 

# Multiple Assignment
'''You can assign values to more than one variable using just a single line. This can help shorten your programs and make them easier to read'''
x, y, z = 1, 2, 3
print(f"Value of x = {x}, y = {y} and z = {z}")

# Constant
'''A constant is like a variable whose value stays the same throughout the life of a program. Python doesn't have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed'''
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)