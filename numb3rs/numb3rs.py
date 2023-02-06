import re
import sys

def main():

    print(validate(input('Ipv4 Address: ').strip()))


def validate(ip):
    ip = ip + "."
    if re.match(r'^(([0-1]?[0-9]?[0-9]\.)|(25[0-5]\.)|(2[0-4][0-9]\.)){4}$', ip):
        return True
    else:
        return False



if __name__ == '__main__':
    main()