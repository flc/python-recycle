import six
import itertools

try:
    from collections.abc import Iterable
except ImportError:
    pass


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
                n = next(size)
            except StopIteration:
                return
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk


def fixed_size_grouper(n, iterable, fillvalue=None):
    """Collect data into fixed-length chunks or blocks"""
    args = [iter(iterable)] * n
    if six.PY3:
        func = itertools.zip_longest
    else:
        func = itertools.izip_longest
    return func(fillvalue=fillvalue, *args)


def flatten(iterable):
    """Flatten one level of nesting"""
    return itertools.chain.from_iterable(iterable)


def flatten_deep(iterable):
    """Flatten any level of nesting"""
    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten_deep(item)
        else:
            yield item


def unique(iterable):
    seen = set()  # memory hotspot
    add = seen.add
    for item in iterable:
        if item in seen:
            continue
        add(item)
        yield item
