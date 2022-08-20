# PROBLEM DESCRIPTION:
url = r"https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true"
# -----------------------------------------------------------------------------------------------------------#


n = int(input("amount of scores: "))

while True:
	arr = input("scores so far: ")
	try:
		# check if input length and n are matching
		if len(arr) == n and int(arr):
			break
		else:
			print("Error: invalid input length.")
	# make sure, input is only accepted if it can be turned into a numerical value
	except ValueError:
		print("Error: wrong input type")


class RunnerUpScore:

	def __init__(self, n, arr):
		self.n = n
		self.arr = arr

	@property
	def current_scores(self):
		current_scores= list(arr)
		current_scores = sorted([int(i)for i in current_scores], reverse=True)
		return current_scores

	@property
	def highest_score(self):
		highest_score = max(self.current_scores)
		return highest_score

	@property
	def runner_up_score(self):
		non_max_scores = []
		for i,v in enumerate(self.current_scores):
			if v < self.highest_score:
				non_max_scores.append(v)
		second_highest_score = non_max_scores[0]
		return second_highest_score

rus = RunnerUpScore(n, arr)
print(rus.runner_up_score)
