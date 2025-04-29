# Looping Through all Key-Value Pairs

user = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}

for key, value in user.items():
    print(f'Key is {key} and Value is {value}')
    
# Looping Through All the Keys in a Dictionary
for name in user.keys():
    print(name.title())

# Looping Through All the Values in a Dictionary
for name in user.values():
    print(name.title())

# A list of Dictionaries
alien_1 = {'color':'green', 'points':5}
alien_2 = {'color':'white', 'points':35}

aliens_list = [alien_1, alien_2]

for alien in aliens_list:
    print(alien)

# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color':'green', 'points':'speed':'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

print('--------------')
# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")