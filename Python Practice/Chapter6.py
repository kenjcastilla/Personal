# Chapter 6

# Dictionaries are collections of key-value pairs. A key can be a number, string, list, or even dictionary.
"""alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0['color'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# To delete a key-value pair, use del dictionary_name[key]
del alien_0['y_position']
print(alien_0)

# If you request a key that doesn't exist in a dictionary, then you will get a key error. 
# For example: print(alien_0['y_position'])
# You can use the .get() method and assign a defualt value to return if the requested key does not exist.
print(alien_0.get('y_position', 'That does not exist in the dictionary.'))

# By default, when looping over a dictionary you are looping using the keys--not the values.
# You can use the .keys() method, but again, the keys are used by default.

# To loop through values in a dictionary, use .values()
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}
print("\nThe following languages are mentioned in the dictionary: ")
for language in favorite_languages.values():
	print(language.title())

# A set is a collection in which each item must be unique, and there is no order. The syntax is that of a dictionary w/o keys.
# You can wrap set() around a big list to create a collection identical to the list but without the duplicates.
for language in set(favorite_languages.values()):
	print(language.title())
print('\n')

# Exercise 6-5. Rivers:
rivers = {
	'nile': 'egypt',
	'mississippi': 'united states of america',
	'yangtze': 'china'
}
for river in rivers:
	print(f"The {river.title()} River runs through {rivers.get(river).title()}.")
print("Rivers in this dictionary include: ")
for river in rivers:
	print(river.title())
print("Countries in this dictionary include: ")
for country in rivers.values():
	print(country.title())

aliens = []

# Make 30 green aliens
for alien in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# Adjusting first 3 aliens in list.
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")


favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages: 
		print(f"\t{language.title()}")
"""

cities = {
	'atlanta': {
		'country': 'united states of america',
		'population': 506_800,
		'fact': "home to the busiest airport in the world"
	},

	'dubai': {
		'country': 'united arab emirates',
		'population': 3_300_000,
		'fact': "home to the burj khalifa, tallest man-made structure in the world"
	},

	'cairo': {
		'country': 'egypt',
		'population': 9_000_000,
		'fact': "largest metropolitan area in the arab world"
	},
}

for city, info in cities.items():
	print(f"\n{city.title()} Information:")
	country = f"{info['country']}"
	pop = f"{info['population']}"
	fact = f"{info['fact']}"

	print(f"Country: {country.title()}")
	print(f"Population: {pop}")
	print(f"Fact: {fact.title()}")



