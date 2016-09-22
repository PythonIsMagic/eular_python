import text
import factors
import fibseries
import primes


def separator():
    print('#'*80)


def eular1():
    print(text.eular1)
    result = factors.sum_multiples([3, 5], 1000)
    print('Sum = {}'.format(result))


def eular2():
    print(text.eular2)
    UPPERLIMIT = 4000000
    fibsum = sum([x for x in fibseries.fibonacci(UPPERLIMIT) if x % 2 == 0])
    print('Sum = {}'.format(fibsum))


def eular3():
    print(text.eular3)
    bignumber = 600851475143
    print('Largest prime factor of {}: {}'.format(
        bignumber, primes.max_prime_factor(bignumber)))


if __name__ == "__main__":
    eular1()
    separator()
    eular2()
    separator()
    eular3()
    separator()
