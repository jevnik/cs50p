import pyfiglet
import random
import sys

figlet = pyfiglet.Figlet()

if len(sys.argv) == 1:  #random font if not specified
    figlet.setFont(font=f'{random.choice(figlet.getFonts())}')

elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    figlet.setFont(font=f'{sys.argv[2]}')

else:
    sys.exit('Invalid usage')

prompt = input('Enter string: ')

print(figlet.renderText(prompt))






# print(figlet.getFonts())

# figlet.setFont(font='big')

# print(figlet.renderText('Luka'))

