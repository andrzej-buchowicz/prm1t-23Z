import sys

from silnia import silnia_rekur


def main():
    for param in sys.argv[1:]:
        if param.isdigit():
            n = int(param)
            print(f"{n}! = {silnia_rekur(n):3d}")
        else:
            print(f"{param} nie jest liczba!")


if __name__ == "__main__":
    main()




