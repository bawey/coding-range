import enum

class TraversalMode(enum.Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    LEVELORDER = 4

class BinarySearchTree(object):

    class Node(object):
        def __init__(self, value):
            self._value = value
            self._left = None
            self._right = None
            self._size = 1
        
        @property
        def size(self):
            return self._size

        def insert(self, value):
            BST = BinarySearchTree
            if value == self._value:
                return False

            _node = value < self._value and self._left or value > self._value and self._right
            if _node:
                ans = _node.insert(value)
                self._size += ans
                return ans
            else:
                if value < self._value:
                    if self._left is None:
                        self._left = BST.Node(value)
                elif value > self._value:
                    if self._right is None:
                        self._right = BST.Node(value)
                self._size += 1
                return True

        def find(self, value):
            BST = BinarySearchTree
            _node = self
            while _node is not None:
                if value == _node._value:
                    return True
                else:
                    _node = value < _node._value and _node._left or _node._right

        def _traverse(self, mode=TraversalMode.INORDER):
            if mode == TraversalMode.PREORDER:
                yield self._value
            if self._left is not None:
                for e in self._left._traverse(mode=mode):
                    yield e
            if mode == TraversalMode.INORDER:
                yield self._value
            if self._right:
                for e in self._right._traverse(mode=mode):
                    yield e
            if mode == TraversalMode.POSTORDER:
                yield e


    def inorder(self):
        for e in self._root and self._root._traverse(mode=TraversalMode.INORDER) or []:
            yield e

    def postorder(self):
        for e in self._root and self._root._traverse(mode=TraversalMode.POSTORDER) or []:
            yield e

    def preorder(self):
        for e in self._root and self._root._traverse(mode=TraversalMode.PREORDER) or []:
            yield e

    def levelorder(self):
        if self._root is None:
            raise StopIteration
        _q = [self._root]
        while len(_q) > 0:
            _node = _q.pop(0)
            yield _node._value
            _ = [_q.append(_n) for _n in [_node._left, _node._right] if _n is not None]


    def __contains__(self, value):
        return self._root.find(value)

    def __init__(self):
        self._root = None

    def __len__(self):
        return self._root and self._root.size or 0

    def __iter__(self):
        for e in self.inorder():
            yield e

    def insert(self, value):
        if self._root is None:
            self._root = BinarySearchTree.Node(value=value)
        else:
            self._root.insert(value)