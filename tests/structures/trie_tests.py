import pytest
from structures.trie import Trie


test_data = [
    ('It is not as simple as I would like it to be'.split(' '), {
        'it': 2,
        'not': 1,
        'simple': 1,
        'burn': None
    }),
    ('Things more things lots of things and nothing'.split(' '), {
        'things': 3,
        'nothing': 1,
        'mor': True,
        'th': True,
        'tr': False
    })
]

@pytest.mark.parametrize('words, stats', test_data)
def test_insert_search_and_starts_with(words, stats):
    trie = Trie()
    for word in words:
        trie.insert(word)
    for _w, _c in stats.items():
        if isinstance(_c, bool):
            assert _c == trie.starts_with(_w)
        elif isinstance(_c, int):
            assert _c == trie.search(_w), 'Expected %s to appear %d times, but got %s' % (_w, _c, str(trie.search(_w)))


