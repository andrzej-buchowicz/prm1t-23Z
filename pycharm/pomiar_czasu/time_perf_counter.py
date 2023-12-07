import time
import random


def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def main():
    print("    N     time [s]")
    for N in [100, 200, 500, 1000, 2000, 5000, 10000]:
        arr = [random.randint(1, 100) for n in range(N)]

        start = time.perf_counter()
        bubble_sort(arr)
        end = time.perf_counter()
        print(f'{N:6d}\t{(end - start):10.6f}')


if __name__ == "__main__":
    main()
