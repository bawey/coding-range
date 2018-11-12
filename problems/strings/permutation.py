import sys

class Permutations(object):
    @classmethod
    def permutate(cls, text):
        charset = [c for c in text]
        results = [[]]

        while charset:
            c = charset.pop()
            new_stack = []
            while results:
                item = results.pop()
                for idx in range(0, len(item)):
                    _temp = [_c for _c in item]
                    _temp.insert(idx, c)
                    new_stack.append(_temp)
                _temp = [_c for _c in item]
                _temp.append(c)
                new_stack.append(_temp)
            results = new_stack
        return [''.join(r) for r in results]

        
if __name__ == '__main__':
    data = sys.argv[1:] or ['dog', 'tayga', 'tundra', 'cat']
    for s in data:
        print 'Permutations of %s: %s' % (s, ', '.join(Permutations.permutate(s)))
        
