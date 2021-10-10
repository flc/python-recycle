import pytest

from recycle import utils


@pytest.mark.parametrize(
    'iterable,length,expected', [
        ('AABBCCDD', 2, ['AA', 'BB', 'CC', 'DD']),
        ([1, 2, 3, 4, 5, 6, 7, 8], 3, [[1, 2, 3], [4, 5, 6], [7, 8]])
    ]
)
def test_split_to_equal_parts(iterable, length, expected):
    assert utils.split_to_equal_parts(iterable, length) == expected


def test_gen_random_id():
    rid = utils.gen_random_id(size=10)
    assert len(rid) == 10


def test_gen_random_string():
    rstr = utils.gen_random_string(length=10)
    assert len(rstr) == 10


@pytest.mark.parametrize(
    'seconds,expected', [
        (0, '00:00:00'),
        (1, '00:00:01'),
        (59, '00:00:59'),
        (300, '00:05:00'),
        (301, '00:05:01'),
        (359, '00:05:59'),
        (660, '00:11:00'),
        (661, '00:11:01'),
        (719, '00:11:59'),
        (3600, '01:00:00'),
        (3900, '01:05:00'),
        (3901, '01:05:01'),
        (3959, '01:05:59'),
        (4260, '01:11:00'),
        (4261, '01:11:01'),
        (4319, '01:11:59'),
        (36000, '10:00:00'),
        (36001, '10:00:01'),
        (36059, '10:00:59'),
        (36060, '10:01:00'),
        (36061, '10:01:01'),
        (36119, '10:01:59'),
        (36660, '10:11:00'),
        (36661, '10:11:01'),
        (39599, '10:59:59'),
        (39600, '11:00:00'),
        (39601, '11:00:01'),
        (39659, '11:00:59'),
        (39660, '11:01:00'),
        (39661, '11:01:01'),
        (39719, '11:01:59'),
        (40260, '11:11:00'),
        (40261, '11:11:01'),
        (43199, '11:59:59'),
    ]
)
def test_pretty_time(seconds, expected):
    assert utils.pretty_time(seconds) == expected


@pytest.mark.parametrize(
    'seconds,expected', [
        (0, '0s'),
        (1, '1s'),
        (10, '10s'),
        (60, '1m 0s'),
        (61, '1m 1s'),
        (70, '1m 10s'),
        (71, '1m 11s'),
        (3600, '1h 0s'),
        (3601, '1h 1s'),
        (3610, '1h 10s'),
        (3660, '1h 1m 0s'),
        (3661, '1h 1m 1s'),
        (3670, '1h 1m 10s'),
        (3671, '1h 1m 11s'),
    ]
)
def test_seconds_to_str(seconds, expected):
    assert utils.seconds_to_str(seconds) == expected


@pytest.mark.parametrize(
    'dec,expected', [
        (32790, [15, 4, 2, 1]),
        (32791, [15, 4, 2, 1, 0]),
    ]
)
def test_dec_to_bin_int_list(dec, expected):
    assert utils.dec_to_bin_int_list(dec) == expected


@pytest.mark.parametrize(
    'dictionary,prefix,expected', [
        ({'a': 1, 'b': 2}, 'x', {'xa': 1, 'xb': 2}),
    ]
)
def test_prefix_dict_keys(dictionary, prefix, expected):
    assert utils.prefix_dict_keys(dictionary, prefix) == expected


@pytest.mark.parametrize(
    's,chars,delimiter,splitter,expected', [
        ('hello monty python xy', 4, '\n', ' ', 'hello\nmonty\npython\nxy'),
    ]
)
def test_words_splitted(s, chars, delimiter, splitter, expected):
    assert utils.words_splitter(s, chars, delimiter, splitter) == expected
