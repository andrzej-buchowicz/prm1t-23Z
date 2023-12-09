
def silnia_iter(n):
    silnia = 1
    for k in range(1, n + 1):
        silnia *= k
    return silnia


def silnia_rekur(n):
    if n > 1:
        return n * silnia_rekur(n - 1)
    else:
        return 1


def main():
    for n in range(10):
        print(n, silnia_iter(n), silnia_rekur(n))


if __name__ == "__main__":
    main()

