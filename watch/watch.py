import re

def main():
    print(parse(input('HTML: ').strip()))



def parse(html):
    out = None
    if match := re.search(r'src="https?://(?:www.)?youtube.com/embed/(\w*)"',html):
        out = 'https://youtu.be/' +match[1]


    return out
if __name__ == '__main__':
    main()