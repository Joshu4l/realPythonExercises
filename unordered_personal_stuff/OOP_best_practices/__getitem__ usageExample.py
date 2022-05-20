# EXAMPLE ON HOW TO USE THE .__getitem__() METHOD IN ORDER TO ACCESS ITEMS OUT OF AN INDEXED OBJECT
helpful_resource = r"https://www.geeksforgeeks.org/__getitem__-and-__setitem__-in-python/"

import datetime
class Customer:

	def __init__(self, name):

		# here, we are setting up an indexable object in form of a dictionary attribute
		self.bank_credentials = {
			'name': name,
			'registration_date': datetime.date.today(),
			'current_balance': 100,
			'transactions_history': [17, 322, 54, 20]
		}

	def __repr__(self):
		return f"how an object is printed because we defined a custom '__repr__()' method:\n" \
			   f"{self.bank_credentials}\n"


	# GET section
	def __getitem__(self, key):
		"""this method is specifically used on instance attributes which consist of an index-able container
		like e.g. list, dictionary, array etc."""
		# Providing a basis for more comfortable dictionary-kvp-access
		return self.bank_credentials[key]  # example for using .__getitem__() on a dictionary


	def get_name(self):  # making use of the .__getitem__() method we defined above
		return self.__getitem__('name')  # advantage is: we don't have to reference the keys via the []-syntax anymore

	def get_registration_date(self):  # making use of the .__getitem__() method we defined above
		return self.__getitem__('registration_date')  # advantage is: we don't have to reference keys via the []-syntax anymore

	def get_current_balance(self):  # making use of the .__getitem__() method we defined above
		return self.__getitem__('current_balance')  # advantage is: we don't have to reference keys via the []-syntax anymore


josh = Customer("Josh")
print(josh)

# Example on making some method calls
print(josh.get_name())
print(josh.get_registration_date())
print(josh.get_current_balance())
