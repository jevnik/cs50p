import datetime
import inflect
import sys

def main():

    p = inflect.engine()
    dob_user = input('Date of Birth: ')
    dob_user = birth_date(dob_user)
    age = datetime.date.today() - dob_user.date()
    minutes = age.days * 24 *60
    word = p.number_to_words(minutes, andword="")
    word = word.capitalize() + ' minutes'

    print(word)

def birth_date(dob):
    try:
        dob = datetime.datetime.strptime(dob,'%Y-%m-%d')

    except ValueError:
        sys.exit('Invalid date')

    return dob


if __name__ == '__main__':
    main()