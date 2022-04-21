# Underlying video tutorial for this exercise module:
url = r"https://www.youtube.com/watch?v=jCzT9XFZ5bw&ab_channel=CoreySchafer"

class Person:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	# example for making an actually accessible attribute out of a function/method by using the @property decorator
	@property
	def email_address(self):
		"""turning a METHOD into an accessible OBJECT ATTRIBUTE"""
		email = f"{self.first_name}.{self.last_name}@email.com"
		return email

	# example for making an actually accessible attribute out of a function/method by using the @property decorator
	@property
	def full_name(self):
		return f"{self.first_name} {self.last_name}"

	# example for an attribute setter/reassigning-method
	@full_name.setter
	def full_name(self, new_name):
		"""First of all, split the input into a list of two components (new_first and new_last)
		Then use the list the two new names and assign the actual attributes to them respectively.
		This also results in a new full name of course (taking care of every necessary attribute in this way)"""
		f, l = new_name.split(' ')
		self.first_name = f
		self.last_name = l


# instantiating a first Person
p = Person("josh", "albert")
# show that persons credentials
print(p.first_name)
print(p.last_name)
print(p.full_name)

# Use the 'full_name' attribute and by that reassign both other attributes that our 'full_name' attribute derives from
p.full_name = "Jon Doe"
print(p.full_name)
