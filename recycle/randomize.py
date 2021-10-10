import random
from datetime import timedelta

from heapq import nlargest


def sample_from_iterable(it, k):
    return (x for _, x in nlargest(k, ((random.random(), x) for x in it)))


def random_date_in_range(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )
