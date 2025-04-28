# Changing, Adding, and Removing Elements

# Modifying Elements in a List
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print(motorcycles)

# Change or Modify element in List
motorcycles[0] = 'Ducati'
print(motorcycles)

# Adding Elements to a List
# append() method add Elements to the End of a List
motorcycles.append('Hero')
print(motorcycles)

# Inserting Elements into a List
# insert() You can add a new element at any position in your list by using the insert() method.
motorcycles.insert(0, 'Bajaj')
print(motorcycles)

# Removing an Item Using the del Statement 
# If you know the position of the item you want to remove from a list, you can use the del statment.
del motorcycles[1]
print(motorcycles)

# Removing an Item Using the pop() method
# The pop() method removes the last item in a list.
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# Removing an Item by Value
# remove() - Sometimes you won't know the position of the value you want to remove item from a list. If you only know the value of the item you want to remove, you can use the remove() method.
# Note - The remove() method deletes only the first occurance of the value you specify. If there's a possibility the value appears more than once in the list, you'll need to use a loop to make sure all occurance of the value are removed.

motorcycles.remove('Honda')
print(motorcycles)


