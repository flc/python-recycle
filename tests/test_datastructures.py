import pytest

from recycle import datastructures


def test_ordered_defaultdict():
    data = (
        ('a', 1),
        ('b', 2),
        ('a', 3),
        ('c', 4),
        ('b', 5),
    )
    dd = datastructures.OrderedDefaultdict(int)
    for k, v in data:
        dd[k] += v
    assert dd['a'] == 4

    dd['d'] = 5
    assert list(dd.keys()) == ['a', 'b', 'c', 'd']


@pytest.mark.parametrize(
    'data,expected', [
        (
            ('c', 'd', 'e', 'c', 'a', 'b', 'd', 'e'),
            {'c', 'd', 'e', 'a', 'b'},
        ),
        (
            (5, 3, 4, 4, 2, 5, 1, 3, 1),
            {5, 3, 4, 2, 1},
        ),
    ]
)
def test_ordered_set(data, expected):
    d = datastructures.OrderedSet(data)
    assert list(set(data)) != list(d)
    assert d == expected


@pytest.mark.parametrize(
    'data,n,expected', [
        (
            range(10),
            2,
            [0, 1]
        ),
        (
            ['c', 'd', 'g', 'a', 'e', 'b', 'g', 'f', 'a'],
            3,
            ['a', 'a', 'b']
        ),
    ]
)
def test_nsmallest(data, n, expected):
    d = datastructures.NSmallest(n)
    for e in data:
        d.add(e)
    assert d.get_result() == expected


@pytest.mark.parametrize(
    'data,n,expected', [
        (
            range(10),
            2,
            [9, 8]
        ),
        (
            ['c', 'd', 'g', 'a', 'e', 'b', 'g', 'f', 'a'],
            3,
            ['g', 'g', 'f']
        ),
    ]
)
def test_nlargest(data, n, expected):
    d = datastructures.NLargest(n)
    for e in data:
        d.add(e)
    assert d.get_result() == expected
