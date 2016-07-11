import sys


def main():
    for arg in sys.argv[1:]:
        with open(arg, 'r') as data:
            print(data.read())


if __name__ == '__main__':
    main()
