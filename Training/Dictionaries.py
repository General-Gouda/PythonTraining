# Dictionary (a lot like hash tables)
student = {
    "name": "Mark",
    "student_id":15163,
    "feedback": None
}

# A list of Dictionary objects
all_students = [
    {"name":"Mark","student_id": 15163},
    {"name":"Katarina","student_id": 63112},
    {"name":"Jessica","student_id": 30021}
]

# Getting data from Dictionaries
print(
    student["name"]
)

# If key does not exist in the dictionary it will write Unknown here
print(
    student.get("last_name", "Unknown")
)

print(
    student.keys(), # shows all keys in the dictionary as a list
)

print(
    student.values() # shows all values in the dictionary as a list
)

student["name"] = "James" # changes name from Mark to James in the name key of the dictionary

del student["name"] # deletes the "name" key in the dictionary

