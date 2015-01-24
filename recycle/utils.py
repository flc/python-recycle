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
