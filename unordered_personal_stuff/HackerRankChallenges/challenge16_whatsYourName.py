# PROBLEM DESCRIPTION:
url = r"https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen"
#-------------------------------------------------------------------------------------------------------------------------------------------#

# Complete the 'print_full_name' function below.

# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last

def print_full_name(first, last):
	print(f"Hello {first} {last}! You just delved into python.")


if __name__ == '__main__':
	first_name = input()
	last_name = input()
	print_full_name(first_name, last_name)
