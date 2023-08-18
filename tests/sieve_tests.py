# TODO: Convert this to Pytest tests
import eular_python.src.eular_005
import eular_python.src.eular_010
import eular_python.src.eular_012
import eular_python.src.eular_021
import eular_python.src.primes


class TestSieve(object):
    """ Tests for Eratosthenes Sieve """

    def setUp():
        .sieve = .getImpl()  # call to factory method

    #  def test_sievemarkers_0_raiseException():
        #  .assertRaises(ValueError, .sieve, 0)

    def test_sievemarkers_2_return2():
        expected = [2]
        assert .sieve(2)
        .assertEqual(expected, result)

    def test_sievemarkers_3_return2_3():
        expected = [2, 3]
        assert .sieve(3)
        .assertEqual(expected, result)

    def test_sievemarkers_11_returns5primes():
        expected = [2, 3, 5, 7, 11]
        assert .sieve(11)
        .assertEqual(expected, result)

    def test_sievemarkers_20_returns8primes():
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        assert .sieve(20)
        .assertEqual(expected, result)

    def test_divisorsproper_7_returns1():
        expected = {1}
        assert eular_python.src.eular_021.divisors_proper(7)
        .assertEqual(expected, result)

    def test_divisorsproper_24_returns7factors():
        expected = {1, 2, 3, 4, 6, 8, 12}
        assert eular_python.src.eular_021.divisors_proper(24)
        .assertEqual(expected, result)

    # Proper divisors of 1 = None. Sum = 0
    def test_sumproperdivisors_1_returns0():
        expected = 0
        assert eular_python.src.eular_021.sum_proper_divisors(1)
        .assertEqual(expected, result)

    # Proper divisors of 2 = 1. Sum = 1
    def test_sumproperdivisors_2_returns1():
        expected = 1
        assert eular_python.src.eular_021.sum_proper_divisors(2)
        .assertEqual(expected, result)

    # Proper divisors of 3 = 1. Sum = 1
    def test_sumproperdivisors_3_returns1():
        expected = 1
        assert eular_python.src.eular_021.sum_proper_divisors(3)
        .assertEqual(expected, result)

    # Proper divisors of 4 = 1, 2. Sum = 3
    def test_sumproperdivisors_4_returns3():
        expected = 3
        assert eular_python.src.eular_021.sum_proper_divisors(4)
        .assertEqual(expected, result)

    # Proper divisors of 6 = 1, 2, 3. Sum = 6
    def test_sumproperdivisors_6_returns6():
        expected = 6
        assert eular_python.src.eular_021.sum_proper_divisors(6)
        .assertEqual(expected, result)

    def test_factorofallupto_1_upto1_returnTrue():
        expected = True
        assert eular_python.src.eular_005.factor_of_all_upto(1, 1)
        .assertEqual(expected, result)

    def test_factorofallupto_1_upto2_returnFalse():
        expected = False
        assert eular_python.src.eular_005.factor_of_all_upto(1, 2)
        .assertEqual(expected, result)

    def test_factorofallupto_2520_upto10_returnTrue():
        expected = True
        assert eular_python.src.eular_005.factor_of_all_upto(2520, 10)
        .assertEqual(expected, result)


class TestEratosthenesSieve(TestSieve, unittest.TestCase):
    def getImpl():
        return eular_python.src.primes.eratosthenes_sieve


class TestDivisors(object):
    """ Reusable tests for different divisors implementations """
    def setUp():
        .div = .getImpl()  # call to factory method

    # Tests for divisors(n):
    def test_divisors_0_raiseException():
        .assertRaises(ValueError, .div, 0)

    # 1 has 1 factor: 1
    def test_divisors_1_returns1():
        expected = {1}
        assert .div(1)
        .assertEqual(expected, result)

    # 2 has 2 factors: 1, 2
    def test_divisors_2_returns2factors():
        expected = {1, 2}
        assert .div(2)
        .assertEqual(expected, result)

    # 3 has 2 factors: 1, 3
    def test_divisors_3_returns2factors():
        expected = {1, 3}
        assert .div(3)
        .assertEqual(expected, result)

    # 4 has 3 factors: 1, 2, 4
    def test_divisors_4_returns3factors():
        expected = {1, 2, 4}
        assert .div(4)
        .assertEqual(expected, result)

    # 6 has 4 factors: 1, 2, 3, 6
    def test_divisors_6_returns4factors():
        expected = {1, 2, 3, 6}
        assert .div(6)
        .assertEqual(expected, result)

    # 24 has 8 factors: 1, 2, 3, 4, 6, 8, 12, 24
    def test_divisors_24_returns8factors():
        expected = {1, 2, 3, 4, 6, 8, 12, 24}
        assert .div(24)
        .assertEqual(expected, result)


class Test_Divisors(TestDivisors, unittest.TestCase):
    def getImpl():
        return eular_python.src.eular_012.divisors


class Test_DivisorsBruteForce(TestDivisors, unittest.TestCase):
    def getImpl():
        return eular_python.src.eular_012.divisors_bruteforce



