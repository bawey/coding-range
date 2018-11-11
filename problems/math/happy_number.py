import sys

class HappyNumber(object):
    def __init__(self, number):
        self._number = number
        self._is_happy = self._determine_happiness()

    def _determine_happiness(self):
        _number = self._number
        _trace = set()
        while True:
            _number = sum([int(c) ** 2 for c in str(_number)])
            if _number == 1:
                return True
            elif _number in _trace:
                return False
            else:
                _trace.add(_number)

    @property
    def is_happy(self):
        return self._is_happy

if __name__ == '__main__':
    num = sys.argv[1]
    hn = HappyNumber(int(num))
    print hn.is_happy
