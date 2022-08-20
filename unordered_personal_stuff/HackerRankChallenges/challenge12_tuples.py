# PROBLEM DESCRIPTION:
r = r"https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true"
#-------------------------------------------------------------------------------------------#

if __name__ == '__main__':
	n = int(input("num of inputs: "))
	integer_list = tuple(map(int, input("inputs: ").split()))

	# print(integer_list)
	hsh = hash(integer_list[:n+1])
	print(hsh)