from multiprocessing import Pool, cpu_count
from operator import itemgetter


def collatz_sequence_length(start):
    n = start
    l = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        l = l + 1

    return start, l


def parallel_collatz_length(max_start):
    pool = Pool(2 * cpu_count() + 1)
    return pool.map(collatz_sequence_length, range(max_start))


def start_for_longest_collatz_sequence(max_start):
    start_length_tuples = parallel_collatz_length(max_start)
    return max(start_length_tuples, key=itemgetter(1))


print(start_for_longest_collatz_sequence(1000000))
