# import gzip
import pytest

from recycle import looping


@pytest.mark.parametrize(
    'size,iterable,expected', [
        (
            2,
            ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E'],
            [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E',)]
        ),
    ]
)
def test_grouper(size, iterable, expected):
    assert list(looping.grouper(size, iterable)) == expected


@pytest.mark.parametrize(
    'size,iterable,expected', [
        (
            2,
            ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E'],
            [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', None)]
        ),
    ]
)
def test_fixed_size_grouper(size, iterable, expected):
    assert list(looping.fixed_size_grouper(size, iterable)) == expected


@pytest.mark.parametrize(
    'iterable,expected', [
        (
            [('A', 'A'), ('B', 'B'), ('C',)],
            ['A', 'A', 'B', 'B', 'C'],
        ),
    ]
)
def test_flatten(iterable, expected):
    assert list(looping.flatten(iterable)) == expected


@pytest.mark.parametrize(
    'iterable,expected', [
        (
            ['A', 'A', 'B', 'B', 'C'],
            ['A', 'B', 'C'],
        ),
    ]
)
def test_unique(iterable, expected):
    assert list(looping.unique(iterable)) == expected
