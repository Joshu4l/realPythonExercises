
def split_camelcase(sequence):

	"""splits an input string written in camel case """

	relevant_indices = [ind for ind, val in enumerate(sequence) if val.isupper()]
	splitup = []

	start = -(len(relevant_indices))
	end = start+1

	while end < 0:

		splitup.append( sequence[relevant_indices[start] : relevant_indices[end]] )
		start +=1
		end +=1

	splitup.append( sequence[relevant_indices[-1]:])

	return splitup




strings = [
	"HelloWorld",
	"ILikeApples",
	"HelloImBobAndImTwentyEight",
	"DogsAndCats"
]
for y in strings:
	print(split_camelcase(y))
