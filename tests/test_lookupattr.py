# import gzip
from recycle import lookupattr


class A:
    pass


class B:
    pass


def test_lookupattr():
    a = A()
    a.name = 'a'
    a.dct = {'a': 1, 'b': 2, 'c': lambda: 3}
    b = B()
    b.a = a
    assert b.a.name == 'a'
    assert lookupattr.lookupattr(b, 'a') == a
    assert lookupattr.lookupattr(b, 'a.name') == 'a'
    assert lookupattr.lookupattr(b, 'a.dct.a') == 1
    assert lookupattr.lookupattr(b, 'a.dct.c') == 3
    assert lookupattr.lookupattr(b, 'a.dct.x') is None
