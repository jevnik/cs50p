import sys

if not len(sys.argv) == 2:
    if len(sys.argv) < 2:
        #print('Too few command-line arguments')
        sys.exit('Too few command-line arguments')
    else:
        #print('Too many command-line arguments')
        sys.exit('Too many command-line arguments')
elif not sys.argv[1].endswith('.py'):
    #print('Not a Python file')
    sys.exit('Not a Python file')

try:
    a = open(sys.argv[1])
except FileNotFoundError:
    #print('File does not exist')
    sys.exit('File does not exist')


counter = 0
for line in a:
    if line[0] == '#':
        continue
    elif len(line.strip()) == 0:
        continue
    elif line.lstrip()[0] == '#':
        continue
    else:
        counter += 1

print(counter)