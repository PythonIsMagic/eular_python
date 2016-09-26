import unittest
import primes


class TestIsPrime:
    def setUp(self):
        self.ip = self.getImpl()  # call to factory method

    """
    Tests for is_prime(target):
    """
    def test_isprime_0_returnFalse(self):
        expected = False
        result = self.ip(0)
        self.assertEqual(expected, result)

    def test_isprime_1_returnFalse(self):
        expected = False
        result = self.ip(1)
        self.assertEqual(expected, result)

    def test_isprime_2_returnTrue(self):
        expected = True
        result = self.ip(2)
        self.assertEqual(expected, result)

    def test_isprime_3_returnTrue(self):
        expected = True
        result = self.ip(3)
        self.assertEqual(expected, result)


class TestIsPrimeVer1(TestIsPrime, unittest.TestCase):
    def getImpl(self):
        return primes.isprime_ver1


class TestIsPrimeVer2(TestIsPrime, unittest.TestCase):
    def getImpl(self):
        return primes.isprime_ver2


class TestSieve:
    def setUp(self):
        self.sieve = self.getImpl()  # call to factory method

    """
    Tests for def sieve_markers(n):
    """
    #  def test_sievemarkers_0_raiseException(self):
        #  self.assertRaises(ValueError, self.sieve, 0)

    def test_sievemarkers_2_return2(self):
        expected = [2]
        result = self.sieve(2)
        self.assertEqual(expected, result)

    def test_sievemarkers_3_return2_3(self):
        expected = [2, 3]
        result = self.sieve(3)
        self.assertEqual(expected, result)

    def test_sievemarkers_11_returns5primes(self):
        expected = [2, 3, 5, 7, 11]
        result = self.sieve(11)
        self.assertEqual(expected, result)

    def test_sievemarkers_20_returns8primes(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        result = self.sieve(20)
        self.assertEqual(expected, result)


class TestEratosthenesSieve(TestSieve, unittest.TestCase):
    def getImpl(self):
        return primes.eratosthenes_sieve


class TestPrimes(unittest.TestCase):
    """
    Tests for max_prime_factor(target):
    """
    def test_maxprimefactor_0_returnNone(self):
        expected = None
        result = primes.max_prime_factor(0)
        self.assertEqual(expected, result)

    def test_maxprimefactor_1_returnNone(self):
        expected = None
        result = primes.max_prime_factor(1)
        self.assertEqual(expected, result)

    def test_maxprimefactor_2_return2(self):
        expected = 2
        result = primes.max_prime_factor(2)
        self.assertEqual(expected, result)

    def test_maxprimefactor_3_return3(self):
        expected = 3
        result = primes.max_prime_factor(3)
        self.assertEqual(expected, result)

    def test_maxprimefactor_4_return2(self):
        expected = 2
        result = primes.max_prime_factor(4)
        self.assertEqual(expected, result)

    def test_maxprimefactor_10_return5(self):
        expected = 5
        result = primes.max_prime_factor(10)
        self.assertEqual(expected, result)

    def test_maxprimefactor_100_return5(self):
        expected = 5
        result = primes.max_prime_factor(100)
        self.assertEqual(expected, result)

    def test_maxprimefactor_1000_return5(self):
        expected = 5
        result = primes.max_prime_factor(1000)
        self.assertEqual(expected, result)

    """
    Tests for primes(n)
    """
    def test_primes_1next_return2(self):
        g = primes.primes()
        expected = 2
        result = next(g)
        self.assertEqual(expected, result)

    def test_primes_2next_return3(self):
        g = primes.primes()
        expected = 3
        next(g)
        result = next(g)
        self.assertEqual(expected, result)

    def test_primes_3next_return5(self):
        g = primes.primes()
        expected = 5
        next(g)
        next(g)
        result = next(g)
        self.assertEqual(expected, result)

    """
    Tests for get_prime_factors(target):
    """
    # of -1 = None
    def test_getprimefactors_neg1_returnsNone(self):
        expected = None
        result = primes.get_prime_factors(-1)
        self.assertEqual(expected, result)

    # of 0 = None
    def test_getprimefactors_0_returnsNone(self):
        expected = None
        result = primes.get_prime_factors(0)
        self.assertEqual(expected, result)

    # of 1 = None
    def test_getprimefactors_1_returnsNone(self):
        expected = None
        result = primes.get_prime_factors(1)
        self.assertEqual(expected, result)

    # of 2 = 2
    def test_getprimefactors_2_returns2(self):
        expected = {2}
        result = primes.get_prime_factors(2)
        self.assertEqual(expected, result)

    # of 3 = 3
    def test_getprimefactors_3_returns3(self):
        expected = {3}
        result = primes.get_prime_factors(3)
        self.assertEqual(expected, result)

    # of 4 = 2
    def test_getprimefactors_4_returns2(self):
        expected = {2}
        result = primes.get_prime_factors(4)
        self.assertEqual(expected, result)

    # of 5 = 5
    def test_getprimefactors_5_returns5(self):
        expected = {5}
        result = primes.get_prime_factors(5)
        self.assertEqual(expected, result)

    # of 6 = 2, 3
    def test_getprimefactors_6_returns2_3(self):
        expected = {2, 3}
        result = primes.get_prime_factors(6)
        self.assertEqual(expected, result)

    # of 7 = 7
    def test_getprimefactors_7_returns7(self):
        expected = {7}
        result = primes.get_prime_factors(7)
        self.assertEqual(expected, result)

    # of 10 = 2, 5
    def test_getprimefactors_10_returns2_5(self):
        expected = {2, 5}
        result = primes.get_prime_factors(10)
        self.assertEqual(expected, result)

    # of 12 = 2, 3
    def test_getprimefactors_12_returns2_3(self):
        expected = {2, 3}
        result = primes.get_prime_factors(12)
        self.assertEqual(expected, result)

    # of 24 = 2, 3
    def test_getprimefactors_24_returns2_3(self):
        expected = {2, 3}
        result = primes.get_prime_factors(24)
        self.assertEqual(expected, result)
