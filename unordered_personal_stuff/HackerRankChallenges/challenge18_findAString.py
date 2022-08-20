# PROBLEM DESCRIPTION:
url = r"https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true"
#-------------------------------------------------------------------------------------------------------------------------------------------#


def count_substring(string, sub_string):

	frame_start = 0
	frame_end = frame_start + len(sub_string)
	result_counter = 0

	while frame_start <= (len(string)-len(sub_string)):

		if sub_string == string[frame_start:frame_end]:
			result_counter +=1

		frame_start +=1
		frame_end +=1

	return result_counter


if __name__ == '__main__':
	string = input().strip()
	sub_string = input().strip()

	count = count_substring(string, sub_string)
	print(count)

