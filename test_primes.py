"""
  " Tests for the prime (and division) related functions
  """
import primes
import pytest


@pytest.fixture(params=[primes.isprime_ver1, primes.isprime_ver2])
def isprime(request):
    return request.param


def test_isprime_0_returnFalse(isprime):
    assert isprime(0) is False


def test_isprime_1_returnFalse(isprime):
    assert isprime(1) is False


def test_isprime_2_returnTrue(isprime):
    assert isprime(2)


def test_isprime_3_returnTrue(isprime):
    assert isprime(3)


def test_fromprime():
    """ Compares divisors and divisors_bruteforce. """
    TRIES = 100
    failures = 0

    for i in range(1, TRIES):
        bf = primes.divisors_bruteforce(i)
        fp = primes.divisors(i)

        if bf != fp:
            print('Test failed on {}!'.format(i))
            print('bruteforce: {}'.format(sorted(bf)))
            print('fromprime:  {}'.format(sorted(fp)))
            failures += 1
        else:
            print('{} - Check.'.format(i))

    if failures > 0:
        print('{} out of {} tests failed.'.format(failures, TRIES - 1))
    else:
        print('All tests passed! (up to {})'.format(TRIES))


def test_maxprimefactor_0_returnNone():
    assert primes.max_prime_factor(0) is None


def test_maxprimefactor_1_returnNone():
    assert primes.max_prime_factor(1) is None


def test_maxprimefactor_2_return2():
    assert primes.max_prime_factor(2) == 2


def test_maxprimefactor_3_return3():
    assert primes.max_prime_factor(3) == 3


def test_maxprimefactor_4_return2():
    assert primes.max_prime_factor(4) == 2


def test_maxprimefactor_10_return5():
    assert primes.max_prime_factor(10) == 5


def test_maxprimefactor_100_return5():
    assert primes.max_prime_factor(100) == 5


def test_maxprimefactor_1000_return5():
    assert primes.max_prime_factor(1000) == 5


def test_primes_1next_return2():
    g = primes.primes()
    assert next(g) == 2


def test_primes_2next_return3():
    g = primes.primes()
    next(g)
    assert next(g) == 3


def test_primes_3next_return5():
    g = primes.primes()
    next(g)
    next(g)
    assert next(g) == 5


# of -1 = None
def test_getprimefactors_neg1_returnsNone():
    assert primes.get_prime_factors(-1) is None


# of 0 = None
def test_getprimefactors_0_returnsNone():
    assert primes.get_prime_factors(0) is None


# of 1 = None
def test_getprimefactors_1_returnsNone():
    assert primes.get_prime_factors(1) is None


# of 2 = 2
def test_getprimefactors_2_returns2():
    assert primes.get_prime_factors(2) is {2}


# of 3 = 3
def test_getprimefactors_3_returns3():
    assert primes.get_prime_factors(3) == {3}


# of 4 = 2
def test_getprimefactors_4_returns2():
    assert primes.get_prime_factors(4) == {2}


# of 5 = 5
def test_getprimefactors_5_returns5():
    assert primes.get_prime_factors(5) == {5}


# of 6 = 2, 3
def test_getprimefactors_6_returns2_3():
    assert primes.get_prime_factors(6) == {2, 3}


# of 7 = 7
def test_getprimefactors_7_returns7():
    assert primes.get_prime_factors(7) == {7}


# of 10 = 2, 5
def test_getprimefactors_10_returns2_5():
    assert primes.get_prime_factors(10) == {2, 5}


# of 12 = 2, 3
def test_getprimefactors_12_returns2_3():
    assert primes.get_prime_factors(12) == {2, 3}


# of 24 = 2, 3
def test_getprimefactors_24_returns2_3():
    assert primes.get_prime_factors(24) == {2, 3}
