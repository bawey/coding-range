class Trie(object):

    class Node(object):
        def __init__(self, value=0):
            self._value = 0
            self._links = [None] * (1 + ord('z') - ord('a'))

        def insert(self, key):
            assert isinstance(key, str)
            if len(key) == 0:
                self._value += 1
            else:
                next_link_idx = Trie.Node._next_link_idx(key)
                if self._links[next_link_idx] is None:
                    self._links[next_link_idx] = Trie.Node()
                self._links[next_link_idx].insert(key[1:])

        def search(self, key):
            assert isinstance(key, str)
            if len(key)==0:
                return self._value
            else:
                next_link_idx = Trie.Node._next_link_idx(key)
                if self._links[next_link_idx] is None:
                    return None
                else:
                    return self._links[next_link_idx].search(key[1:])

        @classmethod
        def _next_link_idx(cls, key):
            return ord(key[0]) - ord('a')

    def __init__(self):
        self._root_node = Trie.Node()

    def search(self, key):
        return self._root_node.search(key)

    def insert(self, key):
        assert isinstance(key, str)
        key = key.strip().lower()
        self._root_node.insert(key)

    def starts_with(self, key):
        return self.search(key) is not None
        


