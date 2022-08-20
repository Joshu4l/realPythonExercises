# PROBLEM DESCRIPTION:
url = r"https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true&h_r=next-challenge&h_v=zen"
#------------------------------------------------------------------------------------------------------------------------------#

def split_and_join(line):
	divided_elements = line.split()
	res = "-".join(divided_elements)
	return res

if __name__ == '__main__':
	line = input()
	result = split_and_join(line)
	print(result)