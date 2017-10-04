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

class HighSchoolStudent(Student): # Derived class HighSchoolStudent inherits class information from the Student class above (parent class)
    school_name = "Springfield High School"

    def get_school_name(self):
        return "This is a High School student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"

# student = Student() # instantiate class to var student

# print(student) # prints location in memory if there is nothing in the class yet

# new_student = Student() # instantiate class to var new_student

# print(new_student) # prints location in memory if there is nothing in the class yet

#####################################

# student = Student()

# student.add_student("Mark") # while function add_student was still in class

#####################################

# mark = Student("Mark")
# print(mark)

#####################################

# print(Student.school_name) # prints out the class attribute school_name that was defined inside of the class as a variable. All class instances will share this attribute.

#####################################

james = HighSchoolStudent("james")

print(james.get_name_capitalize())
# print(james.get_school_name())
