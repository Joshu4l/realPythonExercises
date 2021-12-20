class Test(object):
    # class attribute to keep track of class instances
    instances = []
    def __init__(self, value):
        self.value = value
        Test.instances.append(self)

    # class method to access the get method without any instance
    @classmethod
    def get(cls, value):
        return [inst for inst in cls.instances if inst.value == value]



# # Check if the students actually appear in course's <participants> and <participants_counter> after they enrolled
# for course_result in Course.search_instance_by_name("Introduction to Python 3"):
#     print(f"number of participants in 'Introduction to Python 3': {course_result.participants_counter}")
#     print(f"participant names therein:")
#     for participant in course_result.participants:
#         print(f"- {participant.last_name} {participant.first_name}")
#     # Check if the <professor> instance who started teaching that course actually appears as its attribute value
#     print(f"professor who's teaching that course: {course_result.professor} \n")

search_result_x = Professor.search_instance_by_name("Thomas")
# print(f"search result for all professors called 'Thomas': {search_result_x}")
search_result_j = Person.search_instance_by_name("Josh")
# print(f"search result for all professors called 'Thomas': {search_result_j}")