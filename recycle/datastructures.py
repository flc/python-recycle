import collections

from bisect import insort_left, insort_right

# leave this import here for backward compatibility
from ordered_set import OrderedSet


class OrderedDefaultdict(collections.OrderedDict):

    def __init__(self, *args, **kwargs):
        newdefault = None
        newargs = ()
        if args:
            newdefault = args[0]
            if not callable(newdefault) and newdefault is not None:
                raise TypeError('first argument must be callable or None')
            newargs = args[1:]
        self.default_factory = newdefault
        super(self.__class__, self).__init__(*newargs, **kwargs)

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        self[key] = value = self.default_factory()
        return value


class NSmallest:

    def __init__(self, n):
        self.n = n
        self._result = []

    def add(self, item):
        insort_right(self._result, item)
        if len(self._result) > self.n:
            self._result.pop()

    def get_result(self):
        return self._result


class NLargest:

    def __init__(self, n):
        self.n = n
        self._result = []

    def add(self, item):
        insort_left(self._result, item)
        if len(self._result) > self.n:
            # self._result.pop(0)
            del self._result[0]

    def get_result(self):
        return sorted(self._result, reverse=True)
