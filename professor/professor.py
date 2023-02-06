import random
import sys

def main():
    score = 0
    counter = 0
    lvl = get_level()

    for _ in range(10):
        if counter !=3:

            a = generate_integer(lvl)
            b = generate_integer(lvl)
            c = int(input(f'{a} + {b} = '))

            while c != (a+b):
                counter += 1

                if counter == 3:
                    print(f'{a} + {b} = {a+b}')
                    #print('Score:', score)
                    sys.exit()


                print('EEE')
                c = int(input(f'{a} + {b} = '))


            # if counter == 2:
            #     print(f"{a} + {b} = {a+b}")
            #     break

            if counter !=3:
                score += 1

    print('Score:', score)

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level not in [1,2,3]:
                continue
        except ValueError:
            pass
        else:
            return level

def generate_integer(lvl):
    if lvl == 1:
        return random.randint(10**(lvl-1)-1,10**lvl-1)
    else:
        return random.randint(10**(lvl-1),10**lvl)


if __name__ == '__main__':
    main()