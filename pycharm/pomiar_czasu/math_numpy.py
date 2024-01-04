import math
import numpy as np
import matplotlib.pylab as plt

import timeit


N = [10, 100, 1000, 10000]
math_time = []
for n in N:
    math_time.append(timeit.timeit(stmt="math_data = [math.sin(2 * math.pi * i / n) for i in range(n)]",
                                   setup="import math", number=1000, globals=globals()))
print(math_time)

np_time = []
for n in N:
    np_time.append(timeit.timeit(stmt="t = np.arange(0, 1, 1 / n); np_data = np.sin(2 * np.pi * t)",
                                 setup="import numpy as np", number=1000, globals=globals()))
print(np_time)

_, ax = plt.subplots()
ax.bar(np.arange(len(math_time)) - 0.2, math_time, width=0.4, label='math')
ax.bar(np.arange(len(np_time)) + 0.2, np_time, width=0.4, label='numpy')
ax.legend()
ax.set_xticks(np.arange(len(N)), [str(n) for n in N])
ax.set_xlabel('n')
ax.set_ylabel('czas [s]')
# ax.set_title("Porównanie czasów wykonania obliczeń numerycznych")

_, ax = plt.subplots()
ax.bar(np.arange(len(math_time)) - 0.2, math_time, width=0.4, label='math')
ax.bar(np.arange(len(np_time)) + 0.2, np_time, width=0.4, label='numpy')
ax.legend()
ax.set_xticks(np.arange(len(N)), [str(n) for n in N])
ax.set_xlabel('n')
ax.set_ylabel('czas [s]')
ax.set_yscale('log')


plt.show()

