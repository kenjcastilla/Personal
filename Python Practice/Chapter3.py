# Chapter 3

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)
print(bicycles[0].title())
# Access end of list by using list_name[-1]
print(bicycles[-1])
print(bicycles[-3])

# Using f-strings to create messages based on list elements
message = f"My first bike was a {bicycles[0].title()}"
print(message)


motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)
# Inserting elements shifts everything to the right of it to the right one index.
motorcycles.insert(0, 'harley')
print(motorcycles)
#Deleting an element shifts everything to the right of it to the left one index.
del motorcycles[3]
print(motorcycles)

print("")
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles.remove('ducati')


cars = ['bmw', 'audi', 'toyota', 'subaru']

# list_name.sort() function organizes the list in alphabetical order; you cannot revert back to its original order.
# sorted(list_name) allows you to present the list as sorted while keeping the actual list in its original order.
print(sorted(cars))
print(cars)
cars.sort(reverse = True) 
print(cars)
