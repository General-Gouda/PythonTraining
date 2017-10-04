student_names = ["James","Katarina","Jessica","Mark","Bort","Frank Grimes","Max Power"]

# Interates through the list and when it finds Mark it will display "Found Him!" and break out of the loop
for name in student_names:
    if name == "Mark":
        print("Found him! " + name)
        break
    print("Currently testing " + name)

# Interates through the list and when it finds Bort it continues without processing anything else and goes to the
# next element in the list as if Bort didn't exist.
for name in student_names:
    if name == "Bort":
        continue
        print("Found him! " + name)
    print("Currently testing " + name)

