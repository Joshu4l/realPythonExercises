if __name__ == '__main__':
	s = input()


	class Character:

		characters = []


		def __init__(self, val):
			self.val = val
			Character.characters.append(self)


		@property
		def alphanumeric(self):
			if self.val.isalnum():
				return True
			else:
				return False


		@property
		def alphabetic(self):
			if self.val.isalpha():
				return True
			else:
				return False


		@property
		def digit(self):
			if self.val.isdigit():
				return True
			else:
				return False


		@property
		def low(self):
			if self.val.islower():
				return True
			else:
				return False


		@property
		def up(self):
			if self.val.isupper():
				return True
			else:
				return False


		@classmethod
		def validate(cls):
			subresult = []

			subresult.append([c.alphanumeric for c in Character.characters])
			subresult.append([c.alphabetic for c in Character.characters])
			subresult.append([c.digit for c in Character.characters])
			subresult.append([c.low for c in Character.characters])
			subresult.append([c.up for c in Character.characters])

			result = []
			for j in subresult:
				if any(j):
					result.append(True)
				else:
					result.append(False)
			return result


	for _ in s:
		Character(_)
	print(Character.validate())
