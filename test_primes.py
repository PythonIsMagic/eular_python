import unittest
import primes


class TestPrimes(unittest.TestCase):
    """
    Tests for is_prime(target):
    """
    def test_isprime_0_returnFalse(self):
        expected = False
        result = primes.isprime_2step(0)
        self.assertEqual(expected, result)

    def test_isprime_1_returnFalse(self):
        expected = False
        result = primes.isprime_2step(1)
        self.assertEqual(expected, result)

    def test_isprime_2_returnTrue(self):
        expected = True
        result = primes.isprime_2step(2)
        self.assertEqual(expected, result)

    def test_isprime_3_returnTrue(self):
        expected = True
        result = primes.isprime_2step(3)
        self.assertEqual(expected, result)

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
    Tests for getprime(index):
    """
    def test_getprime_neg1_raiseException(self):
        self.assertRaises(ValueError, primes.getprime, -1)

    def test_getprime_0_returns2(self):
        expected = 2
        result = primes.getprime(0)
        self.assertEqual(expected, result)

    def test_getprime_1_returns3(self):
        expected = 3
        result = primes.getprime(1)
        self.assertEqual(expected, result)

    def test_getprime_2_returns5(self):
        expected = 5
        result = primes.getprime(2)
        self.assertEqual(expected, result)

    """
    Tests for def generate_primes(n)
    """
    def test_generateprimes_0_raiseException(self):
        self.assertRaises(ValueError, primes.generate_primes, 0)

    def test_generateprimes_2_return2(self):
        expected = [2]
        result = primes.generate_primes(2)
        self.assertEqual(expected, result)

    def test_generateprimes_3_return2_3(self):
        expected = [2, 3]
        result = primes.generate_primes(3)
        self.assertEqual(expected, result)

    def test_generateprimes_11_returns5primes(self):
        expected = [2, 3, 5, 7, 11]
        result = primes.generate_primes(11)
        self.assertEqual(expected, result)

    """
    Tests for def sieve_rm_method(n):
    """
    def test__0_raiseException(self):
        self.assertRaises(ValueError, primes.sieve_rm_method, 0)

    def test_sievermmethod_2_return2(self):
        expected = [2]
        result = primes.sieve_rm_method(2)
        self.assertEqual(expected, result)

    def test_sievermmethod_3_return2_3(self):
        expected = [2, 3]
        result = primes.sieve_rm_method(3)
        self.assertEqual(expected, result)

    def test_sievermmethod_11_returns5primes(self):
        expected = [2, 3, 5, 7, 11]
        result = primes.sieve_rm_method(11)
        self.assertEqual(expected, result)

    def test_sievermmethod_20_returns5primes(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        result = primes.sieve_rm_method(20)
        self.assertEqual(expected, result)

    """
    Tests for def sieve_markers(n):
    """
    def test_sievemarkers_0_raiseException(self):
        self.assertRaises(ValueError, primes.sieve_markers, 0)

    def test_sievemarkers_2_return2(self):
        expected = [2]
        result = primes.sieve_markers(2)
        self.assertEqual(expected, result)

    def test_sievemarkers_3_return2_3(self):
        expected = [2, 3]
        result = primes.sieve_markers(3)
        self.assertEqual(expected, result)

    def test_sievemarkers_11_returns5primes(self):
        expected = [2, 3, 5, 7, 11]
        result = primes.sieve_markers(11)
        self.assertEqual(expected, result)

    def test_sievemarkers_20_returns8primes(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        result = primes.sieve_markers(20)
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
