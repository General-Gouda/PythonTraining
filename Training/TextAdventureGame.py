# TEXT ADVENTURE GAME - from https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial/for_Loop
# Modified a bit by me. I added a random number generator so the key location is
# randomly selected each run. Added a few other tweaks here and there to make it run in Python 3.x

import random

# the menu function:
def menu(list, question):
    for entry in list:
        print(1 + list.index(entry),end='')
        print(") " + entry.title())

    return int(input(question)) - 1


# Give the computer some basic information about the room:
items = ["plant", "painting", "vase", "lampshade", "shoe", "door"]

# The key location is randomly generated:
keylocation = random.randint(1, (len(items) - 2))

# You haven't found the key:
keyfound = 0

loop = 1

# Give some introductory text:
print("Last night you went to sleep in the comfort of your own home.")
print("Now, you find yourself locked in a room. You don't know how")
print("you got there, or what time it is. In the room you can see ", end="")
print(len(items), "things:\n")

for x in items:
    print(x)

print("")
print("The door is locked. Could there be a key somewhere?")

# Get your menu working, and the program running until you find the key:
while loop == 1:
    choice = menu(items, "What do you want to inspect? ")
    if choice == 0:
        if choice == keylocation:
            print("You found a small key in the plant!")
            print("")
            
            keyfound = 1
        else:
            print("You found nothing in the plant.")
            print("")
    elif choice == 1:
        if choice == keylocation:
            print("You found a small key behind the painting!")
            print("")

            keyfound = 1
        else:
            print("You found nothing behind the painting.")
            print("")
    elif choice == 2:
        if choice == keylocation:
            print("You found a small key in the vase!")
            print("")

            keyfound = 1
        else:
            print("You found nothing in the vase.")

            print("")
    elif choice == 3:
        if choice == keylocation:
            print("You found a small key in the lampshade!")
            print("")

            keyfound = 1
        else:
            print("You found nothing in the lampshade.")
            print("")

    elif choice == 4:
        if choice == keylocation:
            print("You found a small key in the shoe!")
            print("")

            keyfound = 1
        else:
            print("You found nothing in the shoe.")
            print("")
    elif choice == 5:
        if keyfound == 1:
            loop = 0
            print("You put in the key, turn it, and hear a click")
            print("")
        else:
            print("The door is locked, you need to find a key.")
            print("")

# Remember that a backslash continues
# the code on the next line

print("Light floods into the room as you open the door to your freedom.")
