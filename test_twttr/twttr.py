def main():
    input_string = input('String: ')
    print(shorten(input_string))

def shorten(word):
    res_string = ''
    vowels = 'AEIOUaeiou'
    for i in word:
        if not i in vowels:
            res_string += i
    return res_string

if __name__ == '__main__':
    main()