import csv
import sys

def main():
    check_arg()
    old_list = read_old()
    new_list = first_last_house_list(old_list)

    if check_arg:
        with open(sys.argv[2],'w') as file:
            writer = csv.DictWriter(file,fieldnames=['first','last','house'])
            writer.writeheader()
            for line in new_list:
                writer.writerow(line)

def read_old():
    old_list = []
    with open(sys.argv[1], 'r') as file:
        reader = csv.DictReader(file)
        for line in reader:
            old_list.append(line)
    return old_list

def first_last_house_list(old_list):
    new_list = []
    for line in old_list:
        last, first = line['name'].split(',')
        house = line['house']
        new_list.append({'first': f'{first}', 'last': f'{last}', 'house': f'{house}'})
    return new_list

def check_arg():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif not '.csv' in sys.argv[1] or not '.csv' in sys.argv[2]:
        sys.exit('File is not .csv')
    try:
        with open(f'{sys.argv[1]}','r'):
            pass
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')

if __name__ == '__main__':
    main()