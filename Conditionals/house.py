name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron" :
        print("Gryfindor")
    case "Darco":
        print("Slytherin")
    case _:
        print("Who?")