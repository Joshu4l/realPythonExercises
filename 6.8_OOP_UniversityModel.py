# OOP-model for a university:

class Course:

    instances = []
    course_list = []
    course_number = 0000

    def __init__(self, course_name, course_ects, course_domain):

        Course.instances.append(self)

        self.course_name = course_name.lower()
        # Check if the course already exists, otherwise add its <course_name> to the list of offered courses
        if not course_name.lower() in Course.course_list:
            Course.course_list.append(self.course_name)

        self.course_ects = course_ects
        self.course_domain = course_domain
        self.professor = None
        self.participants = []
        self.participants_count = 0


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

    def teach_course(self, course_name, course_ects, course_domain):
        """causes the following actions to be executed:
        Check if a <Course> instance with such a <course_name> already exists and if not, instantiate one.
        Make the professor start teaching a course by adding that course to his personal list.
        Make the professor appear as the <Course>'s <.professor> attribute-value."""

        # Check if the course is among the instances of <Course> yet
        # Note that a <Course> instantiation always appends a <course_name> to the university's course list
        # So if there's no such value in there, it seems to not exist:
        if not course_name.lower() in Course.course_list:
            # Instantiate a new course with the <course_name>, the professor started teaching
            Course(course_name, course_ects, course_domain)


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
    student_instances = []
    dropout_instances = []
    ects_tbd = 180

    def __init__(self, last_name, first_name, age):  # Initialize a Student
        super().__init__(last_name, first_name, age)  # <-- ...inherit these initialization-parameters from my super class

        Student.student_count += 1
        Student.student_instances.append(self)
        # Beside the inherited attributes, introduce an enrollment number to <self> (= to the initialized instance)
        self.enrollment_number = f"S-{Student.student_count:04d}"
        self.study_status = "Active"

        self.enrolled_courses = []
        self.enrolled_courses_count = 0

        self.accomplished_courses = []
        self.accomplished_courses_count = 0

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
        # check for the sheer existence of the given course
        if course_name.lower() in Course.course_list:

            # pick out every matching course instance <i>
            for i in Course.search_instance_by_name(course_name.lower()):
                # Add the <Student> instance to the course's list of participants
                i.participants.append(self)
                i.participants_count = len(i.participants)
                # Add the given <Course> instance to the student's personal list of enrolled courses
                self.enrolled_courses.append(i)
                self.enrolled_courses_count = len(self.enrolled_courses)

            # Show an enrollment feedback
            print(f"{self.first_name} {self.last_name} was enrolled in course '{course_name}'. \n")

        # if no identically-named course exists
        else:
            print(f"No such course '{course_name}' available to enroll in!")


    def get_grade(self):
        """generates a random exam score and assigns it to a grade"""
        grade = randint(40, 62)
        if grade < 60:
            return "E"
        elif grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            print("wrong score")


    def accomplish_course(self, course_name):
        """shifts a course from the student's enrolled list into his/her accomplished list"""

        # Check if the given course even is among the student's enrolled ones
        for i in self.enrolled_courses:

            # if so, pick the matching course object, and...
            if course_name.lower() == i.course_name:

                # ... delete the student from its participants
                i.participants.pop(i.participants.index(self))
                i.participants_count = len(i.participants)

                # ...delete it from the student's enrolled ones
                self.enrolled_courses.pop(self.enrolled_courses.index(i))
                self.enrolled_courses_count = len(self.enrolled_courses)

                # ...add it to the student's accomplished ones
                self.accomplished_courses.append(i)
                self.accomplished_courses_count = len(self.accomplished_courses)
                print(f"successfully accomplished {course_name}")

            # if there is no such course name among the student's enrolled ones
            else:
                print(
                    f"No such course '{course_name}', in which {self.first_name} {self.last_name} is enrolled in currently")


    def check_number_of_exam_attempts(self, course_name, grade):
        """checks past exam_score-records for the given course and
        evaluates for the case of '3rd attempt with result >E<'
        or alternatively
        evaluates for the case of '2nd attempt with result >E<' """

        for key, value in self.exam_scores[course_name].items():
            if key == "grades":
                course_grades = value

                # scenario for a 3rd failed attempt
                if (len(course_grades) >= 3) and (course_grades[-1] == "E"):
                    print(f"{self.first_name} {self.last_name} failed '{course_name}' three times. Exmatriculation was proceeded")
                    self.exmatricluate(course_name.lower())

                # scenario for a 2nd failed attempt
                else:
                    print(f"{self.first_name} {self.last_name} failed another attempt on '{course_name}' with result >{grade}<.")
                    print(f"current status: {self.exam_scores} \n")


    def exmatricluate(self, course_name):
        """causes the student to:
        change his <study_status> to 'Dropped out',
        remove himself from the list of <Student> instances,
        remove himself from the course's participants-list"""

        Student.student_instances.pop(Student.student_instances.index(self))
        Student.dropout_instances.append(self)
        self.study_status = "Dropped out"

        for course in Course.instances:
            if course.course_name == course_name:
                course.participants.pop(course.participants.index(self))
                course.participants_counter = len(course.participants)
                # course.participants_counter -= 1  # might be smarter to refactor that attribute value to <len(participants)>


    def write_exam(self, course_name):
        # Check if there's even a <Course> instance with a <course_name> equal to the search parameter
        course_tbd = [course.course_name for course in Course.search_instance_by_name(course_name)]
        if course_name.lower() in course_tbd:

            # Get a random score and assign it to a grade
            grade = Student.get_grade(self)

            # Check IF there are already ANY EXISTING GRADES for that <Student> instance with that <course_name>
            if course_name.lower() in self.exam_scores.keys():

                # Catch the CURRENT GRADES-RECORD for that <Student> instance and that <course_name>
                grades_record = self.exam_scores[course_name.lower()]["grades"]

                # if the LATEST ATTEMPT was already PASSED (which means, not an 'E')
                if grades_record[-1] != "E":
                    print(f"{self.first_name} {self.last_name} already passed '{course_name}' successfully!")
                    print(f"current status: {self.exam_scores} \n")

                # if the LATEST ATTEMPTS were FAILED in the past but the CURRENT ATTEMPT IS SUCCESSFUL
                elif (grades_record[-1] == "E") and (grade != "E"):
                    self.exam_scores[course_name.lower()]["grades"].append(grade)
                    self.exam_scores[course_name.lower()]["trials"] += 1
                    print(f"{self.first_name} {self.last_name}'s latest attempt on '{course_name}' was successful: grade >{grade}<")
                    print(f"current status: {self.exam_scores} \n")
                    self.accomplish_course(course_name.lower())

                # if the LATEST ATTEMPTS were FAILED in the past and the CURRENT ATTEMPT IS FAILED AGAIN
                else:
                    self.exam_scores[course_name.lower()]["grades"].append(grade)
                    self.exam_scores[course_name.lower()]["trials"] += 1
                    # Also check if the number of attempts still lies within the range of the course's max. strikes
                    self.check_number_of_exam_attempts(course_name.lower(), grade)


            # if this is the FIRST ATTEMPT FOR THAT COURSE, create an <.exam_scores> entry for
            else:
                self.exam_scores[course_name.lower()] = {"grades": [grade], "trials": 1}
                print(f"{self.first_name} {self.last_name} made a fist attempt on '{course_name}' with result >{grade}<.")
                print(f"current status: {self.exam_scores} \n")

        # if there is no <Course> instance existing with that course_name
        else:
            print(f"no such subject '{course_name}' available for examination")




# Instantiate a course
w1 = Course("Business Informatics", 10, "Informatics")

# Instantiate a new professor
bahlinger = Professor("Bahlinger", "Thomas", 50)
# Let him teach some courses
bahlinger.teach_course("Business Informatics",5,"Informatics")
bahlinger.teach_course("Introduction to Python 3", 5, "Informatics")
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
print("\n")


print(f"student instances: {Student.student_instances} \n")


s2.write_exam("Introduction to Python 3")
s2.write_exam("Introduction to Python 3")
s2.write_exam("Introduction to Python 3")
print(s2.study_status)

s2.enroll_into_course("Business Informatics")
s1.enroll_into_course("Business Informatics")
print(s1.enrolled_courses)
print(s1.enrolled_courses_count)

print(w1.participants_count)
