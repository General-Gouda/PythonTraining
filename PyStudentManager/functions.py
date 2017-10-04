
students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(name, student_id=332):
    student = {"name": name, "student_id": student_id}
    students.append(student)

# Open function access modes:
# - 'w' - writing; overwrites the entire file
# - 'r' - reading a text file
# - 'a' - appending to a new or existing file
# - 'rb' - reading a bindary file
# - 'wb' - writing to a binary file

def save_file(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            print(student)
        f.close()
    except Exception:
        print("Could not read file")


# def var_args(name, **kwargs):
#     print(name)
#     print(kwargs["description"], kwargs["feedback"])

# add_student(name="Mark", student_id=15)

# var_args("Mark", description="Loves Python", feedback = None, pluralsight_subscriber = True)

# student_list = get_students_titlecase()

user_query = input("Would you like to add a student? (Y/N): ")

if user_query.upper() == "Y":
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    add_student(student_name, student_id)
    save_file(student_name + ", " + student_id)
    print_students_titlecase()
    # print_students_titlecase()
    # print("Here are the students currently in the database:")
    # read_file()
elif user_query.upper() == "N":
    read_file()
else:
    print("Bad input! Please try again.")


