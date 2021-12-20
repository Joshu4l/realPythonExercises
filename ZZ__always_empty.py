class Person:
	# IMPORTANT EXAMPLE - component 1 of 2:
	person_count = 0  # create a class attribute and initialize it with 0
	instances = []


	def __init__(self, last_name, first_name, age):
		Person.instances.append(self)

		# IMPORTANT EXAMPLE - component 2 of 2:
		# When initialized, increase the counter on all objects of the person class!
		Person.person_count += 1  # by making it one part of each __init__ process

		self.last_name = last_name
		self.first_name = first_name
		self.age = age


	def __str__(self):
		"""return some basic information about a given <Person> object"""
		return f"{self.first_name} {self.last_name}, age: {self.age}"



from random import randint
class Student(Person):

	student_count = int(0)
	ects_tbd = 180

	strikes_max = 3
	strikes = 0


	def __init__(self, last_name, first_name):  # Initialize a Student
		super().__init__(last_name, first_name)  # <-- ...inherit these initialization-parameters from my super class

		Student.student_count += 1
		# Beside the inherited attributes, introduce an enrollment number to <self> (= to the initialized instance)
		self.enrollment_number = f"S-{Student.student_count:04d}"
		self.enrolled_courses = []
		self.accomplished_courses = []
		self.ects_count = 0
		self.exam_scores = {}
		print(f"Student object '{self.first_name} {self.last_name}', age: {self.age}, enrollment number: {self.enrollment_number} was created. \n")

	def write_exam(self, course_name):

		# if the Student passes the exam
		if course_name.lower() in self.exam_scores.keys():
			# add another score resulting from the current exam attempt
			self.exam_scores[course_name.lower()]["grades"].append(randint(1, 101))
			# increment the number of trials by one
			self.exam_scores[course_name.lower()]["trials"] += 1


		# If a corresponding <Course> instance does not exist
		else:
			print(f"there is no such course '{course_name}' available for examination")







#
#
# p1 = Person("Josh", 26)
#
# print(p1.enrolled_courses)
# print(p1.accomplished_courses)
# #print(p1.accomplished_courses())
# p1.accomplish_course("Python 3")
# print(p1.enrolled_courses)
# print(p1.accomplished_courses)



