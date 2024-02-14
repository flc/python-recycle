import random
import string
import time
from decimal import Decimal, ROUND_HALF_UP
from math import ceil, floor


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
    """Generates a random ID consisting only numbers. The first number can not be zero.

    :param size:
        the length of the generated string
        default is 10
    """
    digits = [str(random.randint(1, 9))]
    digits.extend([str(random.randint(0, 9)) for _ in range(0, size - 1)])
    return ''.join(digits)


def gen_random_string(length=10, alphabet=string.ascii_letters + string.digits):
    """
    Generates a random string from a given alphabet.
    The default alphabet contains ascii letters and digits.

    :param length:
        the length of the generated string
    :param alphabet:
    """
    return ''.join([random.choice(alphabet) for i in range(length)])


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


def prefix_dict_keys(dictionary, prefix):
    """
    Prefixes the keys of the dictionary with prefix.
    """
    return {
        "".join([prefix, k]): v
        for k, v in dictionary.items()
    }


def words_splitter(s, chars=75, delimiter="\n", splitter=" "):
    words = s.split(splitter)
    out = []
    sub = []
    c = 0
    for w in words:
        c += len(w)
        sub.append(w)
        if c >= chars:
            out.append(sub)
            c = 0
            sub = []
    out.append(sub)
    return delimiter.join([splitter.join(s) for s in out])


def decimal_round(number, ndigits=0):
    """"
    This function is to overcome the float rounding issues:
    https://docs.python.org/3/library/functions.html?highlight=round#round

    E.g.:
    In [1]: round(90.335, 2)
    Out[1]: 90.33
    In [5]: round(90.335000000000001, 2)
    Out[5]: 90.34
    In [6]: round(90.3350000000000001, 2)
    Out[6]: 90.33
    """
    if isinstance(number, (float, int)):
        number = str(number)
    if isinstance(number, str):
        number = Decimal(number)
    return number.quantize(Decimal(10) ** -ndigits, rounding=ROUND_HALF_UP)


def round_to_multiple(number, multiple, dir='up'):
    div = number / multiple
    if dir == 'up':
        return multiple * ceil(div)
    elif dir == 'down':
        return multiple * floor(div)
    return multiple * round(div)
