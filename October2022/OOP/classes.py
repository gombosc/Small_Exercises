class Student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


    def type(self):
        if self.grade <= 6:
            print(self.name, "is a below average student with a grade of", self.grade)
        elif self.grade >=6 or self.grade <=8:
            print(self.name, "is an average student with a grade of", self.grade)
        else: print(self.name, "is an exceptional student with a grade of", self.grade)


while True:
    student_name = input("Please insert student name: ")
    student_age = input("Please insert student age: ")
    student_grade = int(input("Please insert student grade: "))

    student1 = Student(student_name, student_age, student_grade)
    student1.type()
    break
