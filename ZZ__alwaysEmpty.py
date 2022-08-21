url = r"https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true"

# It must start with a 4,5  or 6.
# It must contain exactly 16 digits.
# It must only consist of digits (0-9).
# It may have digits in groups of 4, separated by one hyphen "-".
# It must NOT use any other separator like ' ', '_', etc.
# It is NOT allowed to have 4 or more repetitions of a digit in a row


class Card:

	cards = []

	def __init__(self, number):
		self.number = number
		Card.cards.append(self)

	@property
	def identified(self):
		inpt = list(self.number)
		identified = [int(i) if i.isdigit() else i for i in inpt]
		return identified

	@property
	def delimited(self):
		delimiters = [i for i in self.identified if type(i) == str]
		if delimiters:
			return True
		else:
			return False

	@property
	def start_validation(self):
		start_digit = int(self.number[0])
		valid = [i for i in range(4,7)]

		if start_digit in valid:
			return True
		else:
			return False

	@property
	def character_validation(self):

		valid_strings = ["_", "-"]

		eval_collector = []
		for i in self.identified:
			if (type(i) == str) and (i not in valid_strings):
				eval_collector.append(False)
			elif (type(i) == str) and (i in valid_strings):
				eval_collector.append(True)
			else:
				eval_collector.append(True)
		return all(eval_collector)

	@property
	def length_validation(self):

		if not self.character_validation:
			return False

		else:
			strings = [i for i in self.identified if type(i) == str]
			if strings:
				if len(self.number) != 19:
					return False
				else:
					return True
			else:
				if len(self.number) != 16:
					return False
				else:
					return True

	@property
	def group_validation(self):

		if not self.delimited and self.character_validation:
			# If no delimiters were detected AND the character validation was successful, ...
			return True # ... don't even start with any further step and state True

		else:
			intended_positions = [4,9,14]
			actual_positions = []

			for i, v in enumerate(self.identified):
				if type(v) == str:
					actual_positions.append(i)
				else:
					continue

			if actual_positions and (actual_positions == intended_positions):
				return True
			else:
				print(f"<actual_positions> did not match <intended_positions>\n"
					  f"actual: {actual_positions}\n"
					  f"intended: {intended_positions} ")
				return False

	@property
	def repetition_validation(self):
		num = self.number
		for i in num:
			if not i.isdigit():
				num = num.replace(i, "") # cleanse all non-digit characters before actually doing the validation

		start = 0
		end = start + 4
		eval_collector = []

		while end < len(num):

			for i in num[start:end]:

				digit_counter = num[start:end].count(i)  # check how often i occurs within the examined slice

				if digit_counter == 4:
					eval_collector.append(True)  # a digit occurred 4 times and thus negated a validation
				else:
					eval_collector.append(False)

				start += 1
				end += 1

		if not any(eval_collector):  # if not a single sub-comparison resulted in 4 identical digits in a row ...
			return True  # ...let the validation be successful
		else:
			return False

	@property
	def overall_validation(self):
		if all([self.start_validation, self.character_validation, self.length_validation, self.group_validation, self.repetition_validation]):
			return "Valid"
		else:
			return "Invalid"


if __name__ == '__main__':

	N = input("number of cards: ")
	for _ in range(int(N)):
		crd_number = input("card: ")
		Card(crd_number)

	# results = [i.overall_validation() for i in Card.cards]
	# for i in results:
	# 	print(i)

	for c in Card.cards:
		print(c.overall_validation)


	# x = "4123456789123456"
	# x = "5123-4567-8912-3456"
	# x = "61234-567-8912-3456"
	# x = "4123356789123456"
	# x = "5133-3367-8912-3456"
	x = "5123 - 3567 - 8912 - 3456"

	c1 = Card(x)
	print(f"start validation:      {c1.start_validation}")
	print(f"character validation:  {c1.character_validation}")
	print(f"length validation:     {c1.length_validation}")
	print(f"group validation:      {c1.group_validation}")
	print(f"repetition validation: {c1.repetition_validation}")



