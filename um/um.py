import re
import sys

print('-'*100)
def main():
    print(count(input('Text: ')))

def count(text):
    counter = 0
    text = text.lower()
    words = text.split(' ')
    print(f'words ({words})',)
    for word in words:
        print()
        print('word',word)
        try:
            if word[2] in '.,:?!-_':
                if word[:2] == 'um':
                    print('found it', word)
                    counter += 1
        except:
            pass

        try:
            if word[0] in '.,:?!-_':
                if word[1:] == 'um':
                    print('found it', word)
                    counter += 1
        except:
            pass

        try:
            if word[0] in '.,:?!-_' and word[3] in '.,:?!-_':
                if word[1:3] == 'um':
                    print('found it', word)
                    counter += 1
        except:
            pass

        if word.strip() == 'um':
            print('found it', word)
            counter += 1
    return counter

if __name__ == '__main__':
    main()