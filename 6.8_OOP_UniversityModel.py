class Course:

    course_list = []
    course_number = 0000
    instances = []

    max_exam_trials = 3

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



class Professor(Person):

    staff_count = 0
    staff_instances = []

    def __init__(self, last_name, first_name, age):  # Initialize a Professor, and ...
        super().__init__(last_name, first_name, age)  # <-- ...inherit these initialization-parameters from the super class
        Professor.staff_instances.append(self)

        Professor.staff_count += 1  # Beside the inherited attributes, ...
        self.staff_number = f"T-{Professor.staff_count:04d}" # ... introduce a staff number to <self>
        self.supervised_courses = []  # ... introduce a personal course list to <self>
        print(f"Professor object '{self.first_name} {self.last_name}', age: {self.age}, enrollment number: {self.staff_number} was created. \n")

    def teach_course(self, course_name):
        """causes the following actions to be executed:
        Check if a <Course> instance with such a <course_name> already exists and if not, instantiate one.
        Make the professor start teaching a course by adding that course to his personal list.
        Make the professor appear as the <Course>'s <.professor> attribute-value."""

        # Check if the course is among the instances of <Course> yet
        # Note that a <Course> instantiation always appends a <course_name> to the university's course list
        # So if there's no such value in there, it seems to not exist:
        if not course_name.lower() in Course.course_list:
            # Instantiate a new course with the <course_name>, the professor started teaching
            Course(course_name, course_domain=None, course_ects=None)


        for course in Course.search_instance_by_name(course_name):
            # Add the student to the course's participants list
            course.professor = self

        # Check if the course is among the professor's personal course list
        if not course_name.lower() in self.supervised_courses:
            # add the course name to the professor's personal course list
            self.supervised_courses.append(course_name.lower())
            print(f"Professor {self.last_name} began to teach course '{course_name}'. \n"
                  f"His courses now are: {self.supervised_courses} \n")
        else:
            print(f"Professor {self.last_name} is already teaching '{course_name}'!")


    def drop_course(self, course_name):
        """causes a professor to stop teaching a course"""

        # Search for matching courses and ...
        for course in Course.search_instance_by_name(course_name.lower()):
            # ... reset the <Course>'s professor attribute
            if course.professor == self:
                course.professor = None

        if course_name.lower() in self.supervised_courses:
            c = self.supervised_courses.index(course_name.lower())
            self.supervised_courses.pop(c)
            print(f"Professor {self.last_name} stopped teaching '{course_name}'. \n"
                  f"His courses now are: {self.supervised_courses}. \n")
        else:
            print(f"No such course '{course_name}' supervised by Professor {self.last_name}.")


from random import randint
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
        self.accomplished_courses = []
        self.ects_count = 0
        self.exam_scores = {}
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


    def get_grade(self):
        """generates a random exam score and assigns it to a grade"""
        grade = randint(20, 100)
        if grade >= 60:
            return "D"
        elif grade >= 70:
            return "C"
        elif grade >= 80:
            return "B"
        elif grade >= 90:
            return "A"
        else:
            return "E"


    def accomplish_course(self, course_name):
        """shifts a course from the student's enrolled list into his/her accomplished list"""
        self.enrolled_courses.pop(self.enrolled_courses.index(course_name))
        self.accomplished_courses.append(course_name)
        print(f"{self.first_name} {self.last_name} passed '{course_name}'.")

    # Exmatriculate the student if he/she fails an exam 3 or more times
    def exmatricluate(self, course_name, grade):

        # add another score resulting from the current exam attempt
        self.exam_scores[course_name.lower()]["grades"].append(grade)
        # increment the number of trials by one
        self.exam_scores[course_name.lower()]["trials"] += 1

        print(f"{self.first_name} {self.last_name} failed '{course_name}' 3 times. Exmatriculation was proceeded")
        del self


    def fail_exam(self, course_name, grade):
        # Check if there have already been attempts before
        print("x")


    def write_exam(self, course_name):
        # Check if there's even a <Course> instance with a <course_name> equal to the search parameter
        course_tbd = [course.course_name for course in Course.search_instance_by_name(course_name)]
        if course_name.lower() in course_tbd:

            # Get a random score and assign it to a grade
            grade = Student.get_grade(self)

            # Check if there are already any grades existing for that <Student> instance with that <course_name> at all
            if course_name.lower() in self.exam_scores.keys():

                # Catch the current grades-record for that <Student> instance and that <course_name>
                currently = self.exam_scores[course_name.lower()]["grades"]

                # if the LATEST ATTEMPT was PASSED (which means, not an 'E')
                if currently[-1] != "E":
                    print(f"{self.first_name} {self.last_name} already passed '{course_name}' successfully!")
                    print(f"current status: {self.exam_scores} \n")

                # if the LATEST ATTEMPT had been FAILED in the past, append the current attempt
                else:
                    self.exam_scores[course_name.lower()]["grades"].append(grade)
                    self.exam_scores[course_name.lower()]["trials"] += 1
                    print(f"{self.first_name} {self.last_name} made another attempt on '{course_name}' with result >{grade}<.")
                    print(f"current status: {self.exam_scores} \n")

            # if this is the first attempt for that course, create an <.exam_scores> entry for
            else:
                self.exam_scores[course_name.lower()] = {"grades": [grade], "trials": 1}
                print(f"{self.first_name} {self.last_name} made a fist attempt on '{course_name}' with result >{grade}<.")
                print(f"current status: {self.exam_scores} \n")

        else:
            print(f"no such subject '{course_name}' available for examination")




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
# Let s1 enroll into a course
s1.enroll_into_course("Introduction to Python 3")

# Instantiate another new student
s2 = Student("Fütterer", "Sarah", 25)
# Show the number of all people at the university again
print(f"number of <Person> instances: {Person.person_count} \n")
# Let s2 enroll into a course
s2.enroll_into_course("Introduction to Python 3")
# Check s2's study progress
print(s2.check_progress())


print(f"initial scenario: {s2.exam_scores} \n")

s2.write_exam("Introduction to Python 3")
s2.write_exam("Introduction to Python 3")
s2.write_exam("Introduction to Python 3")




