import sys
from utils import countUtils,exception_handler
import argparse

@exception_handler
def readFile(filename):
        with open(filename) as f:
            file = f.read()
        return file

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c","--bytes", help="Number of bytes in the file", action='store_true')
    parser.add_argument("-m", "--chars", help="Number of characters in the file", action='store_true')
    parser.add_argument("-l", "--lines", help="Number of lines in the file", action='store_true')
    parser.add_argument("-w", "--words", help="Number of words in the file", action='store_true')
    parser.add_argument("filename", nargs="?", help="filename for which details to generated")

    args = parser.parse_args()

    if args.filename == None:
        file = sys.stdin.buffer.read()
    else:
        file = readFile(args.filename)

    countUtils(file,args)


if __name__ == '__main__':
    main()
