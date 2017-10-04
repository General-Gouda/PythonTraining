student_names = [] # Empty List variable

student_names = ["Mark","Katarina","Jessica"] # List variable with 3 entries

print(student_names)

student_names.append("Homer") # Adds Homer into the List

print(student_names)

if "Mark" in student_names: # Checks to see if the string "Mark" is in the List student_names
    print(True)
else:
    print(False)

print(len(student_names)) # Len gives the count of the number of elements within a List

del student_names[2] # Deletes the name Jessica and shifts all elements after Jessica to the left.

print(student_names)

print(student_names[1:]) # Skips first element in the list and gives the rest

print(student_names[1:-1]) # Ignores first and last element in List