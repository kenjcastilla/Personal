# Chapter 9

# Python is Object-Oriented 
#	 and allows for the creation and use of classes.
# The "self" keyword is comparable to "this" in Java;
#	 variables accessible with "self" are called attributes.
class Dog:
	"""A simple attempt to model a dog."""

	# The initial or "_init_" method is run automatically
	# 	when an instance is created based on a class.
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		self.name = name
		self.age = age
		self.behavior = 'nice'

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over.")

# Use the class as a template for creating an instance.
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
print(f"My dog is {my_dog.behavior}.")

# If you want to create another class based on another,
#	use inheritance.
#	Below, I create a Husky class based on Dog class.

class Husky(Dog):
	def __init__(self, name, age):
		"""Initialize attributes of the parent class."""
		super().__init__(name, age)

	# To override a method, simply rewrite it.
	def roll_over(self):
		print("Huskies can't roll over.")

my_husky = Husky('White Fang', '1')
my_husky.sit()
my_husky.roll_over()