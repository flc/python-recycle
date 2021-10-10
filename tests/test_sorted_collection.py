from operator import itemgetter

from recycle.sorted_collection import SortedCollection


def test_sorted_collection():
    s = SortedCollection(key=itemgetter(2))
    for record in [
        ('roger', 'young', 30),
        ('angela', 'jones', 28),
        ('bill', 'smith', 22),
        ('david', 'thomas', 32)
    ]:
        s.insert(record)

    assert list(s) == [
        ('bill', 'smith', 22),
        ('angela', 'jones', 28),
        ('roger', 'young', 30),
        ('david', 'thomas', 32)
    ]
