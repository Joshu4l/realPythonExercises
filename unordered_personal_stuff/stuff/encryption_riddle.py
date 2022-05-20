class ASCII_Compare:

	ascii_diff_keys = None

	def __init__(self, unencrypted_seq, encrypted_seq):
		self.unencrypted_seq = str(unencrypted_seq)
		self.encrypted_seq = str(encrypted_seq)

	def get_ascii_diff_keys(self):

		u_seq = [ord(pos) for pos in str(self.unencrypted_seq)]
		e_seq = [ord(pos) for pos in str(self.encrypted_seq)]

		if len(u_seq) == len(e_seq):

			diff_key = []
			for character in range(len(u_seq)):
				diff_key.append(e_seq[character] - u_seq[character])
			ASCII_Compare.ascii_diff_keys = diff_key
			return diff_key

		else:
			raise "No comparison possible, the two lengths of your sequences do not match"

my_comparison = ASCII_Compare("STEINBEIS", "XWTJXIKJY")


my_comparison.get_ascii_diff_keys()
print("\n")


class Decrypter:

	sequence_instances = []

	def __init__(self, sequence):
		self.sequence = str(sequence)
		Decrypter.sequence_instances.append(self)

	def get_ascii_counterpart_list(self):
		return [ord(i) for i in self.sequence]

	def get_ascii_counterpart_str(self):
		ascii_concat = ""
		for letter in self.sequence:
			ascii_concat += str(ord(letter))
		return ascii_concat


class ASCII_Converter(Decrypter):

	def __init__(self, input_param=None):
		super().__init__(input_param)

	def decrypt(self, input_sequence, diff_keys=ASCII_Compare.ascii_diff_keys):
		decrypted_sequence = ""
		try:
			for i in range(len(input_sequence)):
				new_ascii_key = ord(input_sequence[i]) - diff_keys[i]
				decrypted_sequence += chr(new_ascii_key)
			return decrypted_sequence

		except TypeError:
			print("Attention: no basis for determining an encryption key provided")
			return "Please provide parameters for class <ASCII_Compare>"

	def encrypt(self, input_sequence, diff_keys=ASCII_Compare.ascii_diff_keys):
		encrypted_sequence = ""
		try:
			for i in range(len(input_sequence)):
				new_ascii_key = ord(input_sequence[i]) + diff_keys[i]
				encrypted_sequence += chr(new_ascii_key)
			return encrypted_sequence

		except TypeError:
			print("Attention: no basis for determining an encryption key provided")
			return "Please provide parameters for class <ASCII_Compare>"

my_converter = ASCII_Converter()

riddle = "XHRV\PZZ"
secret = "SECURITY"

print(my_converter.decrypt(riddle))
print(my_converter.encrypt(secret))
