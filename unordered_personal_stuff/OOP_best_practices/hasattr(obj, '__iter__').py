# Example on how to check IF AN OBJECT (may of course also be an objects attribute) IS ITERABLE

class IterabilityChecker:
	def __init__(self):
		"""instantiates the class and """

	def check_iterability(self, input_object):
		"""checks if the resulting < IterabilityChecker > object is iterable"""

		if hasattr(input_object, '__iter__'):
			return f"{input_object} is iterable"
		else:
			return f"{input_object} is not iterable"
iter_checker = IterabilityChecker()



x = [1, 2, 3, 4, 5]  # set up an example list
y = 6  # set up an example variable

class Example:  # set up an example class in order to see how the <iter_checker> deals with ATTRIBUTES instead of variables

	def __init__(self):
		"""Initializes an instance"""
		self.example_attribute = [17, 322, 54, 20]

	def __repr__(self):
		"""defines how an object is printed when it is being called without any attributes or methods"""
		return self.example_attribute
my_example_instance = Example()  # instantiate an example class



# NOW, DO SOME EXAMPLE CHECKS:
print(iter_checker.check_iterability(x))  # check if a normal list-variable is iterable
print(iter_checker.check_iterability(y))  # check if a normal int-variable is iterable

# check, if even an objects attribute can be assessed on its iterability
print(iter_checker.check_iterability(my_example_instance.example_attribute))





