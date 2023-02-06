def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):


    if 2 < len(s) < 7:
        pass
    else:
        return False

    if s[0].isalpha() and s[1].isalpha():
        pass
    else:
        return False

    if s.isalnum():
        pass
    else:
        return False
    count = 0
    for character in s:
        if character.isdigit() and count == 0 and character == '0':
            return False
        if character.isdigit():
            count += 1
        if character.isalpha() and count != 0:
            return False

    return True


if __name__ == '__main__':
    main()

