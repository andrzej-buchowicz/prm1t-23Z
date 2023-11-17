from silnia import silnia_iter



# to jest komentarz
def main():
    while True:
        n = int(input("Podaj liczbe: "))
        if n <= 0:
            break
        print(n, silnia_iter(n))


"""
to tez jest komentarz



"""

if __name__ == "__main__":
    main()
