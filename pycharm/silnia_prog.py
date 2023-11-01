import silnia


while True:
    n = int(input("Podaj liczbe: "))
    if n <= 0:
        break
    print(n, silnia.silnia_iter(n))
