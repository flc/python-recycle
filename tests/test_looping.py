# import gzip
import itertools
import pytest

from recycle import looping


@pytest.mark.parametrize(
    'size,iterable,expected', [
        (
            2,
            ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E'],
            [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E',)]
        ),
        (
            itertools.chain([1, 1, 2], itertools.repeat(3)),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            [(1,), (2,), (3, 4), (5, 6, 7), (8, 9, 10), (11, 12)]
        ),
        (
            [1, 2],
            [1, 2, 3, 4],
            [(1,), (2, 3)]
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
        (
            ['AA'],
            ['A', 'A'],
        ),
        (
            'AA',
            ['A', 'A'],
        )
    ]
)
def test_flatten(iterable, expected):
    assert list(looping.flatten(iterable)) == expected


@pytest.mark.parametrize(
    'iterable,expected', [
        (
            [
                ('A', 'A'),
                ('B', ('C', 'D')),
                ('E',), [
                    'F',
                    [
                        'G',
                        ['H', ['I'], ['J', 'K'], 'LL']
                    ]
                ],
                12345
            ],
            ['A', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'LL', 12345],
        ),
        (
            ['AA'],
            ['AA'],
        ),
        (
            'AA',
            ['A', 'A'],
        )
    ]
)
def test_flatten_deep(iterable, expected):
    assert list(looping.flatten_deep(iterable)) == expected


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
