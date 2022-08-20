# PROBLEM DESCRIPTION:
url = r"https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true"
#-------------------------------------------------------------------------------------------------------------------------------------------#

def mutate_string(string, position, character):
	old = string
	old_sub1 = old[0:position]
	old_sub2 = old[position+1:]
	new = old_sub1 + character + old_sub2
	return new


if __name__ == '__main__':
	s = input()
	i, c = input().split()
	s_new = mutate_string(s, int(i), c)
	print(s_new)

print(mutate_string("abracadabra",5, "k"))
