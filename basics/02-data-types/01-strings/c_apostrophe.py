# Avoiding Syntax Errors with Strings
''' If you use an apostrophy within single quotes, you'll produce an error. This happens because Python interprets everything between the first single quote and the apostrophe as a string. It then tries to interpret the rest of the text as Python Code, which causes errors.'''

message = "One of Python's strength is its diverse community"
print(message)
'''The apostrophe appears inside a set of double quotes, so the Python interpreter has no trouble reading the string correctly.
However, if you use single quotes, Python can’t identify where the string should end

message_2 = 'One of Python's strength is its diverse community'

You will see the following output:
File "apostrophe.py", line 1
 message = 'One of Python's strengths is its diverse community.'
 SyntaxError: invalid syntax 

'''


