class Heap(object):
    def __init__(self, data=None, cmp_fn=lambda a,b: a < b and -1 or a > b and 1 or 0):
        self._data = data or []
        self._cmp_fn = cmp_fn
        self._heapify()        
    
    def _cmp(self, a, b):
        return self._cmp_fn(a, b)

    @classmethod
    def _p_idx(cls, ix):
        return (ix - 1) / 2

    @classmethod
    def _lc_idx(cls, ix):
        return ix * 2 + 1

    @classmethod
    def _rc_idx(cls, ix):
        return ix * 2 + 2

    def _heapify(self):
        for i in range(len(self._data), 0, -2):
            # sink the parent if need be
            self._sink(Heap._p_idx(i))

    def _sink(self, idx):
        """
        Swaps with smaller of the children (does check!)
        """
        _ix_a, _ix_b = (Heap._lc_idx(idx), Heap._rc_idx(idx))
        if _ix_a < self.size():
            _cnd_ix = _ix_a
            if _ix_b < self.size() and self._cmp(self._data[_ix_a], self._data[_ix_b]) > 0:
                _cnd_ix = _ix_b
            if self._data[idx] is None or self._cmp(self._data[idx], self._data[_cnd_ix]) > 0:
                self._swim(_cnd_ix)
                return _cnd_ix
        return None

    def _swim(self, idx):
        """
        Swaps with parent without checking!
        """
        _p_idx = Heap._p_idx(idx)
        _t = self._data[_p_idx]
        self._data[_p_idx] = self._data[idx]
        self._data[idx] = _t

    def pop(self):
        _v = self.peek()
        self._data[0] = self._data[self.size() - 1]
        del(self._data[self.size() - 1])
        sink_from = 0
        while sink_from is not None:
            sink_from = self._sink(sink_from)
        return _v
    
    def peek(self):
        return self._data[0] if len(self._data) else None

    def insert(self, e):
        self._data.append(e)
        _p_idx = Heap._p_idx(self.size()-1)
        while self._sink(_p_idx):
            _p_idx = Heap._p_idx(_p_idx)


    def size(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return self.size()