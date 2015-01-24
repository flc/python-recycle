import random

from heapq import nlargest


def sample_from_iterable(it, k):
    return (x for _, x in nlargest(k, ((random.random(), x) for x in it)))
