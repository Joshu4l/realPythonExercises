class Course:

    course_list = []
    course_number = 0000
    max_exam_trials = 3
    instances = []

    def __init__(self, course_name, course_ects, course_domain):

        Course.instances.append(self)

        self.course_name = course_name.lower()
        # Check if the course already exists, otherwise add it to the list of offered courses
        if not course_name.lower() in Course.course_list:
            Course.course_list.append(self.course_name)

        self.course_ects = course_ects
        self.course_domain = course_domain
        self.professor = ""
        self.participants_counter = 0
        self.participants = []

    def __str__(self):
        return f"Course name: {self.course_name}, ECTS: {self.course_ects}, Domain: {self.course_domain}"

    @classmethod
    def search_instance_by_name(cls, search_key):
        """list comprehension for getting all instances by a search key
        Works for all classes inheriting from <Person> !"""
        return [obj for obj in cls.instances if obj.course_name.lower() == search_key.lower()]



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

    @classmethod
    def search_instance_by_name(cls, search_key):
        """list comprehension for getting all instances by a search key
        Works for all classes inheriting from <Person> !"""
        return [obj for obj in cls.instances if (obj.last_name == search_key) or (obj.first_name == search_key)]



class Student(Person):

    student_count = int(0)
    ects_tbd = 180

    strikes_max = 3
    strikes = 0

    def __init__(self, last_name, first_name, enrollment_number):  # Initialize a Student
        super().__init__(last_name, first_name, enrollment_number)  # <-- ...inherit these initialization-parameters from my super class

        Student.student_count += 1
        # Beside the inherited attributes, introduce an enrollment number to <self> (= to the initialized instance)
        self.enrollment_number = f"S-{Student.student_count:04d}"
        self.enrolled_courses = []
        self.ects_count = 0
        print(f"Student object '{self.first_name} {self.last_name}', age: {self.age}, enrollment number: {self.enrollment_number} was created. \n")


    def check_progress(self):
        """check a student's progress in terms of ects"""
        if self.ects_count >= self.ects_tbd:
            return f"Congrats to {self.first_name} {self.last_name}: Graduation achieved! :)"
        else:
            return f"{self.first_name} {self.last_name}'s ECTS-count: {self.ects_count}/{self.ects_tbd} \n"


    def enroll_into_course(self, course_name):
        """Let the student pick up a course"""
        if course_name.lower() in Course.course_list:
            # Add the given course to the students personal list of enrolled courses
            self.enrolled_courses.append(course_name.lower())
            print(f"{self.first_name} {self.last_name} was enrolled in course '{course_name}'. \n")

            for course in Course.search_instance_by_name(course_name):
                # Add the student to the course's participants list
                course.participants.append(self)
                # Increment the course's number of participants
                course.participants_counter += 1
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

        self.ects_count += course_ects
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

    def __init__(self, last_name, first_name, age):  # Initialize a Professor, and ...
        super().__init__(last_name, first_name, age)  # <-- ...inherit these initialization-parameters from the super class
        Professor.staff_instances.append(self)

        Professor.staff_count += 1  # Beside the inherited attributes, ...
        self.staff_number = f"T-{Professor.staff_count:04d}" # ... introduce a staff number to <self>
        self.supervised_courses = []  # ... introduce a personal course list to <self>


    def teach_course(self, course_name):
        """causes a professor to start teaching a course and add that course to his personal list"""

        # Check if the course is among the professor's personal course list
        if not course_name.lower() in self.supervised_courses:
            # add the course name to the professor's personal course list
            self.supervised_courses.append(course_name.lower())
            print(f"Professor {self.last_name} began to teach course '{course_name}'. \n"
                  f"His courses now are: {self.supervised_courses} \n")
        else:
            print(f"Professor {self.last_name} is already teaching '{course_name}'!")

        # Check if the course is among the instances of <Course> yet
        if not course_name.lower() in Course.course_list:
            # Instantiate a new course with the one, the professor started teaching
            Course(course_name, course_domain=None, course_ects=None)


    def drop_course(self, course_name):
        """causes a professor to stop teaching a course"""

        if course_name.lower() in self.supervised_courses:
            c = self.supervised_courses.index(course_name.lower())
            self.supervised_courses.pop(c)
            print(f"Professor {self.last_name} stopped teaching '{course_name}'. \n"
                  f"His courses now are: {self.supervised_courses}. \n")
        else:
            print(f"No such course '{course_name}' supervised by Professor {self.last_name}.")



# Instantiate a course
w1 = Course("Business Informatics", 10, "Informatics")


# Instantiate a new professor
bahlinger = Professor("Bahlinger", "Thomas", 50)
# Let him teach some courses
bahlinger.teach_course("Business Informatics")
bahlinger.teach_course("Introduction to Python 3")
# Let him drop a course
bahlinger.drop_course("Business Informatics")


# Instantiate a new student
s1 = Student("Albert", "Josh", 26)
# Show the number of all people at the university
print(f"number of <Person> instances: {Person.person_count} \n")
s1.enroll_into_course("Introduction to Python 3")

# Instantiate another new student
s2 = Student("Fütterer", "Sarah", 25)
# Show the number of all people at the university again
print(f"number of <Person> instances: {Person.person_count} \n")
s2.enroll_into_course("Introduction to Python 3")
# Check s2's study progress
print(s2.check_progress())


# Check if students actually appear in course's participants list and -counter after they enrolled
for course_result in Course.search_instance_by_name("Introduction to Python 3"):
    print(f"number of participants in 'Introduction to Python 3': {course_result.participants_counter}")
    print(f"participant names therein:")
    for participant in course_result.participants:
        print(f"- {participant.last_name} {participant.first_name}")


search_result_x = Professor.search_instance_by_name("Thomas")
# print(f"search result for all professors called 'Thomas': {search_result_x}")
search_result_j = Person.search_instance_by_name("Josh")
# print(f"search result for all professors called 'Thomas': {search_result_j}")



