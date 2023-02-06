def main():
    print(convert(input()))

def convert(smile):
    smile = smile.replace(':)','🙂')
    smile = smile.replace(':(','🙁')
    return smile
if __name__ == '__main__':
    main()