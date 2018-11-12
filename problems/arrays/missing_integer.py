class MissingInteger(object):
    def __init__(self, data, limit):
        self._data = data
        self._store = 0
        self._max = limit
        self._find_missing()


    def _find_missing(self):
        for n in self._data:
            self._mark_as_seen(n)
    
    def _mark_as_seen(self, number):
        self._store |= 1 << (number - 1)

    @property
    def missing(self):
        _tmp = self._store ^ ((1 << self._max) - 1)
        _missing = []
        if _tmp != 0:
            for _susp in range(1, self._max + 1):
                if _tmp & 1 == 1:
                    _missing.append(_susp)
                _tmp = _tmp >> 1
        return _missing


if __name__ == '__main__':
    for data, limit in [
        ([1, 2, 3], 3),
        ([1, 3], 3),
        ([1, 2, 3, 4, 5, 6, 7], 9),
        ([2, 3, 1, 6, 4, 5, 8, 9], 9),
        (range(1,51) + range(52, 97) + [98], 99)
    ]:
        mn = MissingInteger(data, limit)
        print 'Data: %s, limit: %d, missing: %s' % (str(data), limit, str(mn.missing))



    