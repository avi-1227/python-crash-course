# Working with Dictionaries
# Dictionary - A dictionary in Python is a collection of key-value pairs. Each key is connected to a value and you can use a key to access the value associated with that key.

alien = {
    'color':'green',
    'points':5
}

# Acessing Values in Dictionary
print(alien[color])

# Adding New Key-Value pairs
alien['x_position'] = 0
alien['y_position'] = 25

print(alien)

# Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'yellow'
alien_0['points'] = 12

print(alien_0)

# Modifying values in a Dictionary
alien_0['color'] = 'Red'
print(alien_0)

# Removing Key-Value Pairs
del alien_0['points']

print(alien_0)