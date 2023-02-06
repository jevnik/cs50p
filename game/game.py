import random
import sys

def main():
    while True:
        try:
            a = int(input("Level: "))
            if a > 0:
                break
        except:
            pass

    b = random.randint(1, a)

    if a == 1:
        print("Just right!")
        sys.exit()

    while True:
        try:
            c = int(input("Guess: "))

        except:
            continue

        if c > 0 and c < a:
                if c < b:
                    print("Too small!")

                elif c > b:
                    print("Too large!")

                else:
                    print("Just right!")
                    sys.exit()

main()
