class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)

student1 = Student("Tim", 18, 90)
student2 = Student("Dan", 18, 70)

course = Course("Math", 2)
course.add_student(student1)
course.add_student(student2)
print(f"Students in Math Class are {course.students[0].name} and {course.students[1].name}")
print("The average grade of the class is", course.average_grade())

