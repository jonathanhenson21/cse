class Person(object):
    def __init__(self, name, age, school, smart):
        self.name = name
        self.age = age
        self.school = school
        self.smart = smart

    def work(self, ):
        print("%s goes to work" % self.name)


class Employee(object):
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

        def work(self, ):
            print("%s goes to work" % self.name)
