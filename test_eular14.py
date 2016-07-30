import unittest
import eular14

"""
    # Tests for
    def test_(self):
        self.assertRaises(ValueError)

    def test(self):
        expected =
        result =
        self.assertEqual(expected, result)
"""


class TestEular14(unittest.TestCase):
    pass
    # Tests for next_collatz(n)

    def test_nextcollatz_neg1_raiseException(self):
        self.assertRaises(ValueError, eular14.next_collatz, -1)

    def test_nextcollatz_0_raiseException(self):
        self.assertRaises(ValueError, eular14.next_collatz, 0)

    def test_nextcollatz_1_returns4(self):
        expected = 4
        result = eular14.next_collatz(1)
        self.assertEqual(expected, result)

    def test_nextcollatz_2_returns1(self):
        expected = 1
        result = eular14.next_collatz(2)
        self.assertEqual(expected, result)

    def test_nextcollatz_3_returns10(self):
        expected = 10
        result = eular14.next_collatz(3)
        self.assertEqual(expected, result)

    def test_nextcollatz_4_returns2(self):
        expected = 2
        result = eular14.next_collatz(4)
        self.assertEqual(expected, result)

    def test_nextcollatz_5_returns16(self):
        expected = 16
        result = eular14.next_collatz(5)
        self.assertEqual(expected, result)

    # Tests for collatz_seq(n):
    def test_collatzseq_neg1_raiseException(self):
        self.assertRaises(ValueError, eular14.collatz_seq, -1)

    def test_collatzseq_0_raiseException(self):
        self.assertRaises(ValueError, eular14.collatz_seq, 0)

    def test_collatzseq_1_returns1(self):
        expected = [1]
        result = eular14.collatz_seq(1)
        self.assertEqual(expected, result)

    def test_collatzseq_2_returns2_1(self):
        expected = [2, 1]
        result = eular14.collatz_seq(2)
        self.assertEqual(expected, result)

    def test_collatzseq_3_returns3_10_5_16_8_4_2_1(self):
        expected = [3, 10, 5, 16, 8, 4, 2, 1]
        result = eular14.collatz_seq(3)
        self.assertEqual(expected, result)

    def test_collatzseq_4_returns4_2_1(self):
        expected = [4, 2, 1]
        result = eular14.collatz_seq(4)
        self.assertEqual(expected, result)

    def test_collatzseq_5_returns5_16_8_4_2_1(self):
        expected = [5, 16, 8, 4, 2, 1]
        result = eular14.collatz_seq(5)
        self.assertEqual(expected, result)
