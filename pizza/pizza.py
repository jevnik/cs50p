import sys
from tabulate import tabulate

def main():
    table = []
    if check_command(sys.argv):
        try:
            with open(sys.argv[1]) as raw:
                for line in raw:
                    table.append(line.rstrip().split(','))

            print(tabulate(table[1:], headers= table[0],tablefmt='grid'))

        except FileNotFoundError:
            sys.exit('File does not exist')

def check_command(arg):
    if len(arg) < 2:
        sys.exit('Too few command-line arguments')
    elif len(arg) > 2:
        sys.exit('Too many command-line arguments')
    elif not arg[1].endswith('.csv'):
        sys.exit('Not a CSV file')
    else:
        return True

if __name__ == '__main__':
    main()