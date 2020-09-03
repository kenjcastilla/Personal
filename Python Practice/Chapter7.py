# Chapter 7

# User input is achieved through the use of the input keyword.
"""
message = input("Tell me your name: ")
print(f"{message}")

# User input is always taken in as a string.
# To treat the input as a number, use int() or float().
num = input("Enter number: ")
num = int(num)
print(num)

"""

# To remove all instances of a value from a list,
# 	use a while loop.
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')
print(pets)


# You can fill a dictionary using user input.
responses = {}

polling_active = True

while polling_active:
	name = input("What is your name? ")
	response = input("Which mountain would you like to climb someday? ")

	responses[name] = response

	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

	print("\n--- Poll Results ---")
	for name, response in responses.items():
		print(f"{name} would like to climb {response}.")