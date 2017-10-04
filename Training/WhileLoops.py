# Normal while loop
x = 0

while x < 10:
    print("Count is {0}".format(x))
    x += 1


# Infinite while loop that breaks on the number 42
num = 10

while True:
    if num == 42:
        break
    print("Hello World")

