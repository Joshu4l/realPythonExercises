class UserCredentials:

	private_key = None
	public_key = None

	def __init__(self, user_name):
		self.user_name = user_name
	def __str__(self):
		print(self.user_name)

	def set_private_key(self, private_key):
		self.private_key = int(private_key)

	def set_public_key(self, public_key):
		self.public_key = int(public_key)


# sample prime numbers: 11, 17
