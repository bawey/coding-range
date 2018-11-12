from structures.binary_search_tree import BinarySearchTree as BST
import pytest


@pytest.fixture()
def bst(request):
    data = request.param
    bst = BST()
    for e in data:
        bst.insert(e)
    return bst, data

_test_inputs = [[], [0,0,0], [1, 2, 3, 4, 5, 6], [5,3,6,2,7,1,9], [5, 3, 7, 4, 8, 6, 1]]
_level_order = [[], [0], [1, 2, 3, 4, 5, 6], [5,3,6,2,7,1,9], [5, 3, 7, 1, 4, 6, 8]]

@pytest.mark.parametrize('bst', _test_inputs, indirect=['bst'])
def test_len(bst):
    bst, data = bst
    assert len(bst) == len(set(data))


@pytest.mark.parametrize('bst', _test_inputs, indirect=['bst'])
def test_contains(bst):
    bst, data = bst
    for e in data:
        assert e in bst

@pytest.mark.parametrize('bst', _test_inputs, indirect=['bst'])
def test_inorder_traversal(bst):
    bst, data = bst
    _ref = sorted(set(data))
    for e in bst:
        assert _ref[0] == e, 'Expected the first of %s, found %d' % (str(', '.join([str(x) for x in _ref])), e)
        del(_ref[0])

@pytest.mark.parametrize('bst, ref', zip(_test_inputs, _level_order), indirect=['bst'])
def test_levelorder_traversal(bst, ref):
    bst, data = bst
    _order_str = ', '.join([str(e) for e in bst.levelorder()]) 
    _ref_str = ', '.join([str(e) for e in ref]) 
    assert _ref_str == _order_str
