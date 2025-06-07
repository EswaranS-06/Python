from memory_profiler import profile
import time

import timeit

def example1(n):
    return sum(i for i in range(n))

print(timeit.timeit(lambda: example1(10**6), number=10))

@profile
def example(n):
    data = [i for i in range(n)]
    time.sleep(1)
    return sum(data)

if __name__ == '__main__':
    print(example(10**6))