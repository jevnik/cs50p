names = []

while True:
    try:
        names.append(input('Name: '))
    except EOFError:
        print()
        break
print('Adieu, adieu, to ', end='')
if len(names) == 1:
    print(names[0])

elif len(names) == 2:
    print(names[0],'and',names[1])

elif len(names) > 2:
    for name in names:
        if name != names[-1]:
            print(f'{name}, ', end= '')

    print('and',names[-1])
print()