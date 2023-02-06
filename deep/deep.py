a = input('answer to the Great Question of Life, the Universe and Everything: ')
a = a.casefold()
a = a.rstrip()
a = a.lstrip()
match a:
    case '42' | 'forty-two' | 'forty two':
        print('Yes')

    case _:
        print('No')