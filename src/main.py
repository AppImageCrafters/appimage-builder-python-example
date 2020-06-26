#!/usr/bin/env python3

from pyfiglet import Figlet

def main():
    f = Figlet(font='slant')
    print(f.renderText('Hello World!'))


if __name__ == '__main__':
    main()
