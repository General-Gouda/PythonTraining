newList = ["eeny", "meeny", "minee", "moe"]

def menu(list, question):
    for entry in list:
        print(1 + list.index(entry),end=""),
        print(") " + entry)

    question = int(input(question)) - 1

    return list[question]

answer = menu(newList, "Which do you prefer? ")

print("You prefer " + answer)