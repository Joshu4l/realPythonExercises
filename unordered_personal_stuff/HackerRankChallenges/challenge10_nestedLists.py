# PROBLEM DESCRIPTION:
r = "https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true"
# ------------------------------------------------------------------------------#


class Scores:

	students = []

	def __init__(self, n, s):
		self.name = n
		self.score = s
		self.students.append(self)

	@classmethod
	def rank_students(cls):

		subresult = [s for s in Scores.students]

		result = sorted(subresult, key=lambda instance: instance.score, reverse=False)
		# most important here:
		# lambda takes in every instance and assesses the specified attribute based on the reverse-key
		return result

	@classmethod
	def best_score(cls):
		return min(Scores.rank_students(), key=lambda instance: instance.score).score

	@classmethod
	def best_students(cls):

		best_students = []

		for student in Scores.rank_students():
			if student.score <= Scores.best_score():
				best_students.append(student)
			else:
				continue
		return best_students

	@classmethod
	def second_best_students(cls):
		others = []

		for student in Scores.rank_students():
			if student in Scores.best_students():
				continue
			else:
				others.append(student)

		# make sure the fist student with the second-best score is stored with certainty
		second_bests = [others[0]]

		# in case there are even more students with the same (second-best) score level, also store them
		for i in others:
			if i not in second_bests and i.score <= second_bests[0].score:
				second_bests.append(i)
			else:
				continue

		second_best_students = [i.name for i in second_bests]
		return sorted(second_best_students)


# create some students and their scores
for _ in range(int(input("how many students do you want to initialize? "))):
	name = input("name: ")
	score = float(input("grade: "))
	Scores(name,score)

print(Scores.second_best_students())
