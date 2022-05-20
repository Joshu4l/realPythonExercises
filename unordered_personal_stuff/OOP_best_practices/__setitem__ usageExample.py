# EXAMPLE ON HOW TO USE THE .__getitem__() METHOD IN ORDER TO ACCESS ITEMS OUT OF AN INDEXED OBJECT
helpful_resource = r"https://www.geeksforgeeks.org/__getitem__-and-__setitem__-in-python/"

import datetime
class Customer:

	def __init__(self, name):

		# here, we are setting up an indexable object in form of a dictionary attribute
		self.bank_credentials = {
			'name' : name,
			'registration_date' : datetime.date.today(),
			'balance' : 100,
			'transactions' : []
		}

	def __repr__(self):
		return f"how an object is printed because we defined a custom '__repr__()' method:\n" \
			   f"{self.bank_credentials}\n"


	# GET section
	def __getitem__(self, key):
		# Providing a basis for more comfortable dictionary-kvp-ACCESS
		return self.bank_credentials[key]  # example for using .__getitem__() on a dictionary

	def get_name(self):  # making use of the .__getitem__() method we defined above
		return self.__getitem__('name')  # advantage is: we don't have to reference the keys via the []-syntax anymore

	def get_registration_date(self):  # making use of the .__getitem__() method we defined above
		return self.__getitem__('registration_date')  # advantage is: we don't have to reference the keys via the []-syntax anymore

	def get_balance(self):  # making use of the .__getitem__() method we defined above
		return self.__getitem__('balance')  # advantage is: we don't have to reference the keys via the []-syntax anymore

	def get_transactions(self):  # making use of the .__getitem__() method we defined above
		return self.__getitem__('transactions')  # advantage is: we don't have to reference the keys via the []-syntax anymore


	# SET section
	def __setitem__(self, key, value):
		"""this method is specifically used on instance attributes which consist of an index-able container
		like e.g. list, dictionary>, array etc."""
		# Providing a basis for more comfortable dictionary-kvp-ASSIGNMENTS
		self.bank_credentials[key] = value

	def set_name(self, new_value):
		"""simply sets a new name within the customer's bank_credentials"""
		self.__setitem__('name', new_value)  # making use of the .__setitem__() method we defined above

	def add_transaction(self, value):
		"""adds a transaction to the record and adjusts the balance depending on negative/positive input"""
		self.__getitem__('transactions').append(value) # making use of the .__getitem__() method we defined above
		if value < 0:
			print(f"negative transaction of {value}")
		elif value > 0:
			print(f"positive transaction of {value}")
		else:
			print("neutral transaction")
		self.bank_credentials['balance'] += value  # add the value to the balance (- / + will automatically be respected)



j = Customer("Josh")
print(j.get_balance())

j.add_transaction(-70)
j.add_transaction(30)

print(j.get_transactions())
print(j.get_balance())

