import timeit


math_setup = """
import math
"""

math_code = """
[math.sin(2 * math.pi * x/N) for x in range(N)]
"""

for N in [1000, 2000, 5000, 10000]:
    print(N, timeit.timeit(math_code, setup=math_setup, number=1000, globals=globals()))
