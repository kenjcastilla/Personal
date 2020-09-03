# Chapter 4 and 5

# You can create a List of numbers easily by using the list() and range() functions.
numbers = list(range(1, 11))
print(numbers)

# Skipping numbers to create List using range().
even_numbers = list(range(2,11,2))
print(even_numbers)

# Use for loop with range().
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

"""
List comprehension form:
squares = [value**2 for value in range(1,11)]
"""

# Simple statistical operations on Lists
print(min(squares))
print(max(squares))
print(sum(squares))

# Slices allow you to work with a specific group of list items.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[:-3])

for player in players[:3]:
	print(player.title())

# You can copy a List by using list_name[:]. Ommitting first and second index place in notation means whole list.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(friend_foods)


# Tuples are basically Lists whose size and values can't change; they are aka immutable lists.
# Attempting to change an element value will result in a type error.
dimensions = (200, 50)
print(dimensions)
print(dimensions[0])

# The only way to change the values of a tuple is to completely redefine the tuple.
dimensions = (29, 49)
print(dimensions)
print(dimensions[0] == 29)
print(49 in dimensions)
print(50 in dimensions)

if 20 not in dimensions:
	print("20 isn't in dimensions.")

if dimensions:
	print("not empty")
else:
	print("empty")

