import random
import string
import time


def split_to_equal_parts(iterable, length):
    """Splits an iterable to equal length parts.

    :param iterable:
        the iterable to split (list, string, etc.)
    :param length:
        the length of the parts, last part can be truncated obviously
    :return:
        the list of the parts
    """
    return [iterable[i:i + length] for i in range(0, len(iterable), length)]


def gen_random_id(size=10):
    """
    :param size:
        the length of the generated string
        default is 10
    """
    digits = [unicode(random.randint(1, 9))]
    digits.extend([unicode(random.randint(0, 9)) for _ in xrange(0, size - 1)])
    return ''.join(digits)


def gen_random_string(length=10):
    """
    Generates a random string that contains only
    ascii letters and digits.

    :param length:
        the length of the generated string
    """
    return ''.join([random.choice(string.ascii_letters + string.digits)
                    for i in range(length)])


def pretty_time(seconds):
    return time.strftime('%H:%M:%S', time.gmtime(seconds))


def seconds_to_str(seconds):
    output = ''
    if seconds < 60:
        output = "%ds" % seconds
    elif 60 * 60 > seconds >= 60:
        output = "%dm %ds" % (seconds / 60, seconds % 60)
    elif seconds >= 60 * 60:
        output = "%dh " % (seconds / 3600) + seconds_to_str(seconds % 3600)
    return output


def dec_to_bin_int_list(dec):
    """
    Converts a decimal value into a binary string and returns a
    list of integers where the binary bit is 1.
    eg: 32791 -> 1000000000010111 -> [15, 4, 2, 1, 0]
    """
    bits = bin(dec)[2:]
    return [pos for pos, v in zip(range(len(bits) - 1, -1, -1), bits) if int(v)]
