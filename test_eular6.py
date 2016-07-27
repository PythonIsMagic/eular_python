import unittest
import eular6


class TestEular6(unittest.TestCase):
    # Tests for sum_of_squares(upto):
    def test_sumofsquares_upto0_returns0(self):
        expected = 0
        result = eular6.sum_of_squares(0)
        self.assertEqual(expected, result)

    def test_sumofsquares_upto1_returns1(self):
        expected = 1
        result = eular6.sum_of_squares(1)
        self.assertEqual(expected, result)

    def test_sumofsquares_upto2_returns5(self):
        expected = 5
        result = eular6.sum_of_squares(2)
        self.assertEqual(expected, result)

    # Tests for square_of_sum(upto):
    def test_squareofsum_upto1_returns0(self):
        expected = 0
        result = eular6.square_of_sum(0)
        self.assertEqual(expected, result)

    def test_squareofsum_upto1_returns1(self):
        expected = 1
        result = eular6.square_of_sum(1)
        self.assertEqual(expected, result)

    def test_squareofsum_upto2_returns9(self):
        expected = 9
        result = eular6.square_of_sum(2)
        self.assertEqual(expected, result)
