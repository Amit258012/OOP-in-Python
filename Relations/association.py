"""
Association is a relationship between two classes that need to communicate with each other.

Students and courses are associated. Students can enroll in courses, and courses have a list of enrolled students.

[student] <-----> [course] // student takes courses
"""


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        course.add_student(self)


student1 = Student("Amit")
course1 = Course("Python")
student1.enroll(course1)

print(student1.courses[0].course_name)  # Output: Python
print(course1.students[0].name)  # Output: Amit
