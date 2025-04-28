# What is a List?
'''A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabets, the digits from 0-9 or the names of any thing. You can put anything you want into a list'''
# In Python, squart brackets [] indicate a list, and individual elements in the list are separately by commas.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
# Its return its representation of the list, including the square brackets.

# Accessing Elements in a List
'''Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired.'''

print(bicycles[0])
print(bicycles[0].title())

# Python has a special sytax for accessing the last element in a list. By asking for the item at index -1, Python always returns the last item in the list
print(bicycles[-1])
