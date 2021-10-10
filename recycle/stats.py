import numpy as np


def gen_histogram_mem_eff(
    numbers, min_value, max_value, num_bins,
    coerce=float, progress_callback=None, progress_size=10000,
):
    """
    Generates histogram data from an iterable of numbers memory efficiently
    with a predefined range and number of bins.
    It doesn't read the entire set into memory.

    :param numbers: iterable of numbers, preferably a generator
    :param min_value: min_value
    :param max_value: max_value
    :param num_bins: number of bins
    :param coerce: float or int typically or any func that converts the number
    :param progress_callback: None or function that accepts 1 arg: progress
    :param progress_size: when to call progress callback
    """
    bins = np.linspace(min_value, max_value, num_bins)
    hist = np.zeros(num_bins - 1, dtype='int32')
    for idx, val in enumerate(numbers, 1):
        if progress_callback:
            if idx % progress_size == 0:
                progress_callback(idx)

        if coerce:
            val = coerce(val)

        h, __ = np.histogram(val, bins)
        hist += h

    return hist, bins
