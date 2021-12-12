class Person:

    # @classmethod
    # def add_person(cls):
    #     Person.person_count += 1

    # IMPORTANT EXAMPLE - component 1 of 3:
    person_count = 0  # creating a class attribute and initialize it with 0

    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

        # IMPORTANT EXAMPLE - component 2 of 2:
        # Possibility for creating a counter on all objects of that class!
        Person.person_count += 1  # by making it one part of each __init__ process


    def __str__(self):
        return f"{self.first_name} {self.last_name}, age: {self.age}"




class Student(Person):

    student_count = int(0)

    ects_tbd = 180
    ects_done = 0

    strikes_max = 3
    strikes = 0


    def __init__(self, last_name, first_name, enrollment_number):
        super().__init__(last_name, first_name, enrollment_number)

        Student.student_count += 1
        self.enrollment_number = f"S-{self.student_count:04d}"


    # Check the progress for a student in terms of his/her ECTS
    def check_progress(self):

        if self.ects_done >= self.ects_tbd:
            print(f"Congrats to {self.first_name} {self.last_name}: Graduation achieved! :)")
        else:
            print(f"- Hang on {self.first_name}! Only {self.ects_tbd - self.ects_done} more credits to go.")

    # def write_exam(self, course_name, course_ects, result):
    #     if result == "passed":
    #         return self.exam_passed(course_name, course_ects)
    #     else:
    #         return self.exam_failed()


    # Let the student pass a certain subject with its respective credits
    def exam_passed(self, course_name, course_ects):

        self.ects_done += course_ects
        print(f"{self.first_name} {self.last_name} passed {course_name} with {course_ects} ects.")
        return self.check_progress()


    # Exmatriculate the student if he/she fails an exam 3 or more times
    def exmatricluate(self):
        if self.strikes >= self.strikes_max:
            print(f"{self.first_name} {self.last_name} failed the exam 3 times. Exmatriculation is being proceeded")
            del self

    # Method for letting a student fail an exam
    def exam_failed(self, course_name):
        self.strikes += 1
        return self.exmatricluate()



class Professor(Person):

    staff_number = 0

    supervised_courses = []

    def __init__(self, last_name, first_name, staff_number):
        super().__init__(last_name, first_name, staff_number)

    def teach_course(self, course_name):
        self.supervised_courses.append(course_name)

    def drop_course(self, course_name):
        if course_name in self.supervised_courses:
            c = self.supervised_courses.index(course_name)
            self.supervised_courses.pop(c)
            return f"Professor {self.last_name} dropped {course_name}"
        else:
            print(f"No such course '{course_name}' supervised by Professor {self.last_name}")




class Course:

    course_list = []
    course_number = 0000

    max_exam_trials = 3
    participants = 0
    professor = ""

    def __init__(self, course_name, course_ects, course_domain):
        self.course_name = course_name
        self.course_ects = course_ects
        self.course_domain = course_domain
        Course.course_list.append(self.course_name)

    def __str__(self):
        return f"Course name: {self.course_name}, ECTS: {self.course_ects}, Domain: {self.course_domain}"

    def failure(self):
        pass




# jon = Student("Doe", "Jon", 27)
# jon.exam_passed("Maths", 5)
# jon.exam_passed("Python Basics", 160)
# jon.exam_passed("Business Informatics", 10)



# bahlinger = Professor("Bahlinger", "Thomas", 50)
# print(bahlinger)
#
# bahlinger.teach_course("Wirtschaftsinformatik")
# print(bahlinger.supervised_courses)
#
# bahlinger.teach_course("Maths")
# print(bahlinger.supervised_courses)
#
# bahlinger.drop_course("Maths")
# print(bahlinger.supervised_courses)

w1 = Course("Wirtschaftsinformatik", 10, "Informatik")
w2 = Course("Maths II", 5, "Mathematics")


s1 = Student("Albert", "Josh", 26)
# print(s1.enrollment_number)
print(Person.person_count)

s2 = Student("Fütterer", "Sarah", 25)
print(Person.person_count)
print(s1.enrollment_number)
print(s2.enrollment_number)
print(s1)




