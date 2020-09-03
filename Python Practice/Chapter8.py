# Chapter 8

# Use functions like a cache. Easy access to specific jobs you need to get done. 
def greet_user(): 
	"""Display a simple greeting."""
	print("Hello")

greet_user()

# To pass information to a function, put it in the parentheses on call.
def greet_user(username):
	"""Display a simple greeting."""
	print(f"Hello, {username}!")

greet_user('Kendall')


def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

# When using positional arguments, the order should match that of the parameters.
describe_pet('cayman', 'catastrophe')
describe_pet('catastrophe', 'cayman')

#You can also use keyword arguments which specify parameter and argument pair. 
#	Order doesn't matter here.
describe_pet(pet_name='catastrophe', animal_type='cayman')

# Default values allow the parameters to have a default argument that can be changed if 
# 	another argument is passed in from the function call.
def describe_pet(pet_name, animal_type='dog'):
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')


# You can return any type in a function, including collections like dictionaries.
def build_person(first_name, last_name, age=None):
	"""Return a dictionary of information about a person."""
	person = {'first':first_name, 'last':last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
print(build_person('john', 'hooker', 85))


# Modifying a passed in list inside a function creates permanent modifications.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Printing model: {current_design.title()}")
	completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model.title())


# Send a collection type to a function like so:
#	function_name(list_name[:])

# If you don't know how many arguments a function will need to accept, then
#	use *arg_name for arbitrary arguments.
def make_pizza(*toppings):
	"""Print the list of toppings that have been requested."""
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# If you want to use positional and arbitrary args in one function, 
#	arbitrary must come at the end.

# When you don't know how many or what kind of arbitrary args you need to pass,
# 	use **arg_name
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein', 
	location = 'princeton', 
	field = 'physics')
print(user_profile)

# You'll often see **kwargs, which is used to collect
# 	non-specific keyword arguments

""" 
You can access functions from other modules by 
	either importing modules (import module_name)
	and then using module_name.function_name()
	OR
	importing the function alone using 
	from module_name import function_name

You can create and use nicknames for 
	functions and modules by using 
	the as keyword:
		import module_name as mn
		from module_name import function_name as fn
"""




