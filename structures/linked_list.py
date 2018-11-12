class LinkedList(object):

    class Node(object):
        def __init__(self, val):
            self._value = val
            self._next = None
            self._head = None
        
        def link_to(self, node):
            self._next = node

        @property
        def value(self):
            return self._value

        @property
        def next(self):
            return self._next

    def __init__(self, data=None):
        self._length = 0
        self._head = None
        self._tail = None
        if data:
            for el in data:
                self.insert(el)

    def insert(self, value):
        _n = LinkedList.Node(value)
        if not self._head:
            self._head = self._tail = _n
        else:
            self._tail.link_to(_n)
            self._tail = _n
        self._length += 1              


    def __iter__(self):
        _current = self._head
        while _current is not None:
            yield _current.value
            _current = _current.next

    def __len__(self):
        return self._length
        
