# PROBLEM DESCRIPTION:
url = r"https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true"

class Permutation:

	def __init__(self, x, y, z, n):
		self.max_permutation_sum =  n
		self.x_value = x
		self.y_value = y
		self.z_value = z

	@property
	def x_space(self):
		x_permutations = [int(i) for i in range(self.x_value+1)]
		return x_permutations

	@property
	def y_space(self):
		y_permutations = [int(i) for i in range(self.y_value+1)]
		return y_permutations

	@property
	def z_space(self):
		z_permutations = [int(i) for i in range(self.z_value+1)]
		return z_permutations

	@property
	def permutations(self):
		basis = [self.x_space, self.y_space, self.z_space]

		import itertools
		result = list(itertools.product(*basis))

		result_new = []
		for i in result:
			i_new = list(i)
			result_new.append(i_new)

		return result_new

	@property
	def restrictive_permutations(self):
		from copy import deepcopy
		basis = deepcopy(self.permutations)

		result = [i for i in basis if sum(i) != self.max_permutation_sum]
		return result

# Initialize
p = Permutation(int(input("x: ")), int(input("y: ")), int(input("z: ")), int(input("n: ")))

# Compute
print(p.permutations)
print(p.restrictive_permutations)
