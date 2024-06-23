"""
Aggregation:- Each part can exist independently, if school is destroyed then students will not get destroyed.

It impements "has-a" relationship.

[School]<>------>[Students] // School has students

"""


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)


class Student:
    def __init__(self, name):
        self.name = name


student = Student("Ram")
school = School()
school.add_student(student)
print(school.students[0].name)  # Output: Ram
