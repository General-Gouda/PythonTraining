# import hs_student # import from file in same folder. Will need to add hs_student. in front of all methods and functions used.

from hs_student import HighSchoolStudent # Imports the HighSchoolStudent function inside of hs_student so it can be used inside of main.py

# from hs_student import * # Imports ALL functions within the hs_student file

james = HighSchoolStudent("james")
print(james.get_name_capitalize())