from student import *

class HighSchoolStudent(Student): # Derived class HighSchoolStudent inherits class information from the Student class above (parent class)
    school_name = "Springfield High School"

    def get_school_name(self):
        return "This is a High School student"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"
