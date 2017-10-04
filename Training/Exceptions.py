student = {
    "name": "Mark",
    "student_id":15163,
    "feedback": None
}

# Catches the KeyError acception because the program cannot find
# the last_name key and instead handles it with the code inside the except block
try:
    last_name = student["last_name"]
except KeyError:
    print("Error finding last name")

print("this code executes!")

# Type handling exception example
student["last_name"] = "Kowalksi"

try:
    last_name = student["last_name"]
    numbered_last_name = 3 + last_name
except KeyError:
    print("Error finding last name")
except TypeError as error:
    print("I can't add these two together!")
    print(error)
except Exception: # handles all errors if not explicitly defined above
    print("Unknown error")

print("this code executes!")
