# PROBLEM DESCRIPTION:
r = r"https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true"
#-------------------------------------------------------------------------------------------#

from statistics import mean, StatisticsError

class Student:

	students = []

	def __init__(self, nm, sc):
		self.name = nm.lower()
		self.scores = sc
		Student.students.append(self)

	@property
	def avg_score(self):
		try:
			avg = mean(self.scores)
			return avg
		except StatisticsError:
			return None

	@classmethod
	def search_student_score(cls, nm):
		res = [f"{s.avg_score:.2f}" for s in cls.students if nm.lower() == s.name]
		return res

# number of students
n = int(input("number of students: "))
# dict setup
student_marks = {}

# read in the number of students kvps
for _ in range(n):
	# student information is provided as ONE string name <space> grade1 <space> grade2 <space> grade3
	line = input("please enter: <name> <grade1> <grade2> <grade3> ").split()
	# using the 'line'-list, <name> is assigned first, then everything after the name goes into <scores>
	name, scores = line[0], line[1:]
	# apply the float-type to each element in <scores>
	scores = list(map(float, scores))
	# instantiate our Student class
	Student(name,scores)

# let the user provide a student's name to search for
query_name = input("search for a student: ")
# use the input above as an argument for the Student class's search method
for i in Student.search_student_score(query_name):
	print(i)

