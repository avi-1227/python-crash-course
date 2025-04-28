# Organizing a List

# Sorting a List Permanently with the sort() method
# Python's sort() method makes it relatively easy to sort a list. Imagine we have a list of cars and want to change the order of the list to store them alphabetically.

cars = ['bmw', 'audi', 'toyota', 'scoda']
cars.sort()
print(cars)

# You can also sort this list in reverse alphabetical order by passing the argument reverse=True to the sort() method.
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
# To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. The sorted() function lets you display your list in a particular order but doesn't affect the actual order of the list
print(sorted(cars))

# Printing a List in Reverse Order
# To reverse the original order of a list, you can use the reverse() method. reverse() method is changes the order of a list permanently, but you can revert to the original order anytime by applying reverse() to the same list a second time. 
cars.reverse()
print(cars)

# Finding the Length of a List
# You can quickly find the length of a list by using the len() function.
print(len(cars))