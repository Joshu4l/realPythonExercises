# PROBLEM DESCRIPTION:
url = r"https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true"
#--------------------------------------------------------------------------------#

if __name__ == '__main__':
	def swap_case(string):
		swapped = ""

		for s in string:

			try:
				if s.isupper():
					swapped += s.lower()
				else:
					swapped += s.upper()

			except AttributeError:
				print(s)
				swapped += s

		return swapped

	print(swap_case("Www.HackerRank.com"))