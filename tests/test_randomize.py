import datetime
import random
import pytest

from recycle import randomize


random.seed(0)


@pytest.mark.parametrize(
    'iterable,k,expected', [
        (range(100), 2, [94, 17]),
        ((1, 2, 3, 4, 5), 1, [2]),
    ]
)
def test_sample_from_iterable(iterable, k, expected):
    assert list(randomize.sample_from_iterable(iterable, k)) == expected


@pytest.mark.parametrize(
    'start,end,expected', [
        (
            datetime.datetime(2021, 1, 1),
            datetime.datetime(2021, 12, 31),
            datetime.date(2021, 3, 27)
        ),
        (
            datetime.datetime(2021, 1, 1),
            datetime.datetime(2021, 1, 2),
            datetime.date(2021, 1, 1)
        ),
    ]
)
def test_random_date_in_range(start, end, expected):
    assert randomize.random_date_in_range(start, end).date() == expected
