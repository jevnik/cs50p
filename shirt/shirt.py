import sys
from PIL import Image, ImageOps
def main():
    if check_arg():
        # open imgs

        before_img = Image.open(sys.argv[1])
        shirt_img = Image.open('shirt.png')
        before_img_size = before_img.size
        shirt_img_size = shirt_img.size

        muppet = ImageOps.fit(before_img,shirt_img_size)

        muppet.paste(shirt_img, shirt_img)
        # GENERATE NEW IMAGE

        muppet.save(sys.argv[2])





def check_arg():
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif not sys.argv[1][-3:] == sys.argv[2][-3:]:
        sys.exit('Input and output have different extensions')

    elif not any([sys.argv[1].casefold().endswith('.jpg'),sys.argv[1].casefold().endswith('.jpeg'),sys.argv[1].casefold().endswith('.png')]):
        sys.exit('Invalid output')

    else:
        try:
            with Image.open(sys.argv[1]):
                pass
        except FileNotFoundError:
            sys.exit('Input does not exist')

        return True

if __name__ == '__main__':
    main()
