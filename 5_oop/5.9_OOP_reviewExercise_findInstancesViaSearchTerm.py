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

