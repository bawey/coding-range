import sys

# todo: apply Sieve of Eratosthenes

class PrimesCounter(object):
    def __init__(self, cutoff):
        self._cutoff = cutoff
        self._primes_count = self._count_prime_numbers()
    
    @property
    def primes_count(self):
        return self._primes_count

    def _count_prime_numbers(self):
        _count = 0
        for i in range(3, self._cutoff):
            # print '%d is prime? %s' % (i, PrimesCounter.is_prime(i))
            if PrimesCounter.is_prime(i):
                _count += 1
        return _count


    @staticmethod
    def is_prime(suspect):
        for i in range(2, int(suspect ** 0.5) + 1):
            if suspect % i == 0:
                return False
        return True


if __name__ == '__main__':
    pc = PrimesCounter(int(sys.argv[1]))
    print pc.primes_count
