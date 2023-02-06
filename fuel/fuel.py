
while True:

    try:
        x,y = input('fraction: ').split('/')
        x = int(x)
        y = int(y)
        percent = round((x/y)*100)
    except ZeroDivisionError:
        pass

    except ValueError:
        pass

    else:
        if y < x or y == 0:
            pass
        else:
            break

if percent >= 99:
    print('F')
elif percent <= 1:
    print('E')
else:
    print(percent,'%',sep='')
