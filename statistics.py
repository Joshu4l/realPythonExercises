import pandas as pd
from pprint import pprint

df = pd.read_csv(r"C:\Users\Joshua Albert\Desktop\stat.csv")
print(df)
print("\n")


def check_redundancy(val1,val2):
	val1,val2 = val2,val1
	return val1,val2


def calculate_distances(dataframe, column):
	"""takes in a dataframe and a specific column
	and calculates the feature's distances with one another"""

	col_values = dataframe[column].tolist()
	results = {}

	# pick a first item of the given column...
	for value in col_values:

		# ...pick the next item of the column to compare it with
		for other_value in col_values:

			# ignore comparisons of items with themselves (because it will result in 0)
			if value == other_value:
				continue

			# ignore comparisons that are already contained the other way round
			elif check_redundancy(value,other_value) in results:
				continue

			# append the absolute distance to the result-dictionary
			else:
				pair = value,other_value
				distance = abs(value - other_value)
				results[pair] = distance

	return results

pprint(calculate_distances(df,'m1'))

# find the respective row of a value in a dataframe
print(df.index[df["m1"]==28].tolist())
