import itertools


def grouper(size, iterable):
    """
    :param size:
        an integer for fixed size chunks (length of last chunk may differ)
        OR
        an iterable for dynamic sized chunks:
            for example an infinite one: chain([10, 100], repeat(10000))
            but non-infinite ones are also ok but in this case the iteration
            may stop before yielding all the chunks if the sum of the sizes
            are less than the length of the iterable
    :param iterable:
        the iterable to chunk
    :return: generator of chunks
    """
    sizeiter = False
    if hasattr(size, "__iter__"):
        size = iter(size)
        sizeiter = True

    it = iter(iterable)

    while True:
        n = size
        if sizeiter:
            try:
                n = size.next()
            except StopIteration:
                return
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk


def fixed_size_grouper(n, iterable, fillvalue=None):
    """Collect data into fixed-length chunks or blocks"""
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)


def flatten(iterable):
    """Flatten one level of nesting"""
    return itertools.chain.from_iterable(iterable)


def unique(iterable):
    seen = set()  # memory hotspot
    add = seen.add
    for item in iterable:
        if item in seen:
            continue
        add(item)
        yield item
