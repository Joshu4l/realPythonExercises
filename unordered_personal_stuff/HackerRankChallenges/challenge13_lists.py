# PROBLEM DESCRIPTION:
url = r"https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true"
#-----------------------------------------------------------------------------------#

if __name__ == '__main__':

	lst = []
	N = int(input())

	for _ in range(N):

		inpt = list(input().split())

		if inpt[0] == 'insert':
			val = inpt[1:]
			lst.insert(int(val[0]), int(val[1]))

		elif inpt[0] == 'print':
			print(lst)

		elif inpt[0] == 'remove':
			val = int(inpt[1])
			lst.remove(val)

		elif inpt[0] == 'append':
			val = inpt[1:]
			lst.append(int(val[0]))

		elif inpt[0] == 'sort':
			lst.sort()

		elif inpt[0] == 'pop':
			lst.pop()

		elif inpt[0] == 'reverse':
			lst.reverse()

		else:
			continue

