#This is a collection of data type examples with explanations.

"""In Python, there is no need for specific data type name preceding the variable name. 
Just set the name of the variable equal to the value, whatever data type it may be: """
fruit = "apple" 
num = 1
floatingNum = 2.30
letter = 'k'

#The four collection data types in Python are Lists, Tuples, Sets, and Dictionaries.

"""A List is basically an array whose size is not fixed. In other words, you can add to the List after declaration/initialization.
List syntax is as follows: """
fruitList = ["apples", "oranges", "pomegranates", "bananas"]
numList = [1, 2, 6, -3, 9]
floatList = [4.332, 3.14, 67.44]
charList = ['l', 'i', 's', 't']

"""A Tuple is an ordered collection with a fixed size. Once initialized, the size of the Tuple cannot be changed.
Tuple syntax is as follows: """
fruitTuple = ("apples", "oranges", "pomegranates", "bananas")
numTuple = (1, 2, 3, -5, 9 -200)
floatTuple = (3.14, 5.767, 99.999, -300.89)
charTuple = ('t', 'u', 'p', 'l', 'e')

"""A Set is an unordered collection with no fixed size. You can add and pop elements, but the elements are in no specific order.
Comparable to a Java HashSet.
Set syntax is as follows: """
fruitSet = {"apples", "oranges", "pomegranates", "bananas"}
numSet = {1, 2, 78, -256, 34}
floatSet = {1.22, 3.14, -89.6, 212.068}
charSet = {'s', 'e', 't'}
#To iterate over a set, we use the "in" keyword.

"""A dictionary is also an unordered collection with no fixed size. 
Dictionaries have keys and values, so you can access a value through its key name.
Comparable to a Java HashMap.
Dictionary syntax is as follows: """
myDictionary = {
	"fruit": "apple",
	"num": 9,
	"floatNum": 3.14159265,
	"charVal": 'k'
}

if "fruit" in myDictionary:
print(myDictionary["fruit"])



