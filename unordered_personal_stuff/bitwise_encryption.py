unencrypted = "STEINBEIS"
encrypted = "XWTJXIKJY"

original_asciis = []
resulting_asciis = []

for letter in unencrypted:
	original_asciis.append(ord(letter))
for letter in encrypted:
	resulting_asciis.append(ord(letter))

pairs = []
for i in range(len(original_asciis)):
	pairs.append([original_asciis[i],resulting_asciis[i]])

shift_diffs = []
concat_key = ""

for i in pairs:
	shift_diff = i[1]-i[0]
	shift_diffs.append(shift_diff)
	concat_key +=str(shift_diff)
concat_key = int(concat_key)
print(concat_key)

given_chiffre = "XHRV\PZZ"

# EITHER:
# for i,l in enumerate(given_chiffre):
# 	new_letter = ord(l)-shift_diffs[i]
# 	print(chr(new_letter))

# OR:
for i in range(len(given_chiffre)):
	print(chr((ord(given_chiffre[i])- shift_diffs[i])))



