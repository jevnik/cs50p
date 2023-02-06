def main():

    #try:
    fuel = input('fraction: ')
    x,y = fuel.split('/')
    x = int(x)
    y = int(y)
    gauge(convert(fuel))

    # except ZeroDivisionError:
    #     pass

    # except ValueError:
    #     pass

    # else:
    #     if y < x or y == 0:
    #         pass
    #     else:
    #         break

def convert(fraction):
    x,y = fraction.split('/')
    x = int(x)
    y = int(y)
    return round((x/y)*100)

def gauge(p):
    if p >= 99:
        return 'F'
    elif p <= 1:
        return 'E'
    else:
        a = f'{p}%'
        return a


if __name__ == '__main__':
    main()