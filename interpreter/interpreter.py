i = input('Input a math expresion: ')
x, y, z = i.split()
x = float(x)
z = float(z)
match y:
    case '+':
        print(x+z)
    case '-':
        print(x-z)
    case '*':
        print(x*z)
    case '/':
        print(x/z)