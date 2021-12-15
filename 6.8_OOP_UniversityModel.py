class Course:

    course_list = []
    course_number = 0000

    max_exam_trials = 3

    professor = ""

    def __init__(self, course_name, course_ects, course_domain):

        self.course_name = course_name.lower()
        # Check if the course already exists, otherwise add it to the list of offered courses
        if not course_name.lower() in Course.course_list:
            Course.course_list.append(self.course_name)

        self.course_ects = course_ects
        self.course_domain = course_domain

        self.professor = ""
        self.participants_counter = 0
        self.participants_names = []

    def __str__(self):
        return f"Course name: {self.course_name}, ECTS: {self.course_ects}, Domain: {self.course_domain}"

    def failure(self):
        pass



class Person:

    # IMPORTANT EXAMPLE - component 1 of 2:
    person_count = 0  # create a class attribute and initialize it with 0
    instances = []

    def __init__(self, last_name, first_name, age):
        # IMPORTANT EXAMPLE - component 2 of 2:
        # When initialized, increase the counter on all objects of the person class!
        Person.person_count += 1  # by making it one part of each __init__ process

        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        Person.instances.append(self)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, age: {self.age}"

    @classmethod
    def search_instance_by_name(cls, search_key):
        """list comprehension for getting all class instances by a search key"""
        return [obj for obj in cls.instances if obj.last_name == search_key]



class Student(Person):

    student_count = int(0)

    ects_tbd = 180
    ects_done = 0

    strikes_max = 3
    strikes = 0

    def __init__(self, last_name, first_name, enrollment_number):  # Initialize a Student
        super().__init__(last_name, first_name, enrollment_number)  # <-- ...inherit these initialization-parameters from my super class

        Student.student_count += 1
        # Beside the inherited attributes, introduce an enrollment number to <self> (= to the initialized instance)
        self.enrollment_number = f"S-{Student.student_count:04d}"
        self.enrolled_courses = []


    # Check the progress for a student in terms of his/her ECTS
    def check_progress(self):

        if self.ects_done >= self.ects_tbd:
            print(f"Congrats to {self.first_name} {self.last_name}: Graduation achieved! :)")
        else:
            print(f"- Hang on {self.first_name}! Only {self.ects_tbd - self.ects_done} more credits to go.")

    def enroll_into_course(self, course_name):

        if course_name.lower() in Course.course_list:
            self.enrolled_courses.append(course_name.lower())
            print(f"{self.first_name} {self.last_name} was enrolled in course '{course_name}'.")
        else:
            print(f"No such course '{course_name}' available to enroll in!")

    # def submit_exam_score(self, course_name, exam_score):
    #     if int(exam_score) <= 60:
    #         return False
    #     else:
    #         return True



    # def write_exam(self, course_name, result):
    #     if result == "passed":
    #         return self.exam_passed(course_name)
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

    staff_count = 0
    staff_instances = []

    def __init__(self, last_name, first_name, age):  # Initialize a Professor
        super().__init__(last_name, first_name, age)  # <-- ...inherit these initialization-parameters from my super class

        Professor.staff_count += 1

        # Beside the inherited attributes, introduce a staff number to <self> (= to the initialized instance)
        self.staff_number = f"T-{Professor.staff_count:04d}"
        self.supervised_courses = []

        Professor.staff_instances.append(self)

    def teach_course(self, course_name):
        self.supervised_courses.append(course_name.lower())
        if not course_name.lower() in Course.course_list:
            Course.course_list.append(course_name.lower())

        print(f"{self.first_name} {self.last_name} began to teach course '{course_name}'. "
              f"His courses now are: {self.supervised_courses}")

    def drop_course(self, course_name):
        if course_name.lower() in self.supervised_courses:
            c = self.supervised_courses.index(course_name)
            self.supervised_courses.pop(c)
            return f"Professor {self.last_name} dropped {course_name}"
        else:
            print(f"No such course '{course_name}' supervised by Professor {self.last_name}")



# jon = Student("Doe", "Jon", 27)
# jon.exam_passed("Maths", 5)
# jon.exam_passed("Python Basics", 160)
# jon.exam_passed("Business Informatics", 10)



bahlinger = Professor("Bahlinger", "Thomas", 50)
# print(bahlinger)

bahlinger.teach_course("Wirtschaftsinformatik")
# print(bahlinger.supervised_courses)

# bahlinger.teach_course("Maths")
# print(bahlinger.supervised_courses)

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
print(s2)



bahlinger.teach_course("Humbuk 1")

res = Person.search_instance_by_name("Bahlinger")
print(res)




