students = []

class Student:
    # pass # pass keyword tells Python to do nothing 
    # self refers to an instance of a class (to our class from our class)
    # __init__ is the class' constructor
    # def __init__(self, name, student_id=332): 
    #     student = {"name": name, "student_id": student_id}
    #     students.append(student)
    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=332): 
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student: " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name
