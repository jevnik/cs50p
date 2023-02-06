def main():

    greet = input('greeting: ')
    


def value(greeting):
    greeting = greeting.lstrip().casefold()
    if greeting.startswith('hello'):
        return 0
    elif greeting.startswith('h'):
        return 20
    else:
        return 100




if __name__ == '__main':
    main()