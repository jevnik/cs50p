import re
import sys

def main():
    a = input('Hours: ')
    if a:
        print(convert(a))
    else:
        raise ValueError('wrong format')



def convert(time):

    if out := re.search(r'(((1[0-2])|([1-9])) (AM|PM) to ((1[0-2])|([1-9])) (AM|PM))',time):
        #print(out.groups())
        # out.groups()[1] -> sat od
        # out.groups()[4] -> AM|PM od

        # out.groups()[-4] -> sat do
        # out.groups()[-1] -> AM|PM do

        start_h = int(out.groups()[1])
        start_m = out.groups()[4]

        end_h = int(out.groups()[-4])
        end_m = out.groups()[-1]

        if start_m == 'PM' and start_h < 12:
            start_h += 12
        if start_m == 'AM' and start_h == 12:
            start_h = 0

        if end_m == 'PM' and end_h < 12:
            end_h += 12
        if end_m == 'AM' and end_h == 12:
            end_h = 0

        return (f'{start_h:02d}:00 to {end_h:02d}:00')

    elif out := re.search(r'(((1[0-2])|([0-9])):([0-5][0-9]) (AM|PM) to ((1[0-2])|([0-9])):([0-5][0-9]) (AM|PM))',time):
        #print(out.groups())
        # out.groups()[1] -> sat od
        # out.groups()[4] -> minute od
        # out.groups()[5] -> AM|PM od

        # out.groups()[-3] -> sat do
        # out.groups()[-2] -> minute do
        # out.groups()[-1] -> AM|PM do

        start_h = int(out.groups()[1])
        start_min = int(out.groups()[4])
        start_m = out.groups()[5]

        end_h = int(out.groups()[-5])
        end_min = int(out.groups()[-2])
        end_m = out.groups()[-1]

        if start_m == 'PM' and start_h < 12:
            start_h += 12

        if start_m == 'AM' and start_h == 12:
            start_h = 0

        if end_m == 'PM' and end_h < 12:
            end_h += 12

        if end_m == 'AM' and end_h == 12:
            end_h = 0

        return (f'{start_h:02d}:{start_min:02d} to {end_h:02d}:{end_min:02d}')

    else:
        raise ValueError('wrong format')


if __name__ == '__main__':
    main()