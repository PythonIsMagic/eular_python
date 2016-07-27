import unittest
import eular2


class TestEular2(unittest.TestCase):
    # Tests for fibonacci():
    def test_fibonacci_call1_return1(self):
        expected = 1
        calls = 0
        for i, result in enumerate(eular2.fibonacci()):
            if i >= calls:
                self.assertEqual(expected, result)
                break

    def test_fibonacci_call2_return1(self):
        expected = 1
        calls = 1
        for i, result in enumerate(eular2.fibonacci()):
            if i >= calls:
                self.assertEqual(expected, result)
                break

    # Tests for calcsum(upto):
    def test_calcsumofevens_upto0_return0(self):
        expected = 0
        result = eular2.calc_sum_of_evens(0)
        self.assertEqual(expected, result)

    def test_calcsumofevens_upto1_return0(self):
        expected = 0
        result = eular2.calc_sum_of_evens(1)
        self.assertEqual(expected, result)

    def test_calcsumofevens_upto2_return2(self):
        expected = 2
        result = eular2.calc_sum_of_evens(2)
        self.assertEqual(expected, result)
