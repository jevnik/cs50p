from validator_collection import checkers
def main():
    if valid(input('e-mail: ')):
        print('Valid')
    else:
        print('Invalid')

def valid(mail):
    return checkers.is_email(mail)



if __name__ == '__main__':
    main()