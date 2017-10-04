student_names = ["Mark", "Katarina", "Jessica"]

for name in student_names:
    print("Student name is {0}".format(name))  # Interates through each element in the List. There is no ForEach in Python. For does it automatically.


x = 0

for index in range(10):  # Range(10) if it were printed would look like [0,1,2,3,4,5,6,7,8,9]
    x += 10
    print("The value of X is {0}".format(x))

print("")

for index in range(10):
    x = index
    print("The value of X is {0}".format(x))  # see?

print("")

# This time the range starts at the number 5 and goes to 9. The first number in the range must be.
# inside the range itself. 5 is inside the range 0 the 9 but 10 is outside so nothing is printed.
for index in range(5, 10):
    x = index
    print("The value of X is {0}".format(x))

print("")

# starts at 5 and increments by 2 (starting number, end of interations, increments of)
for index in range(5, 10, 2):
    x = index
    print("The value of X is {0}".format(x))


