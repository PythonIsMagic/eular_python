import unittest
import eular5


class TestEular5(unittest.TestCase):
    # Tests for isfactorofall(number, upto):
    def test_isfactorofall_1_upto1_returnTrue(self):
        expected = True
        result = eular5.isfactorofall(1, 1)
        self.assertEqual(expected, result)

    def test_isfactorofall_1_upto2_returnFalse(self):
        expected = False
        result = eular5.isfactorofall(1, 2)
        self.assertEqual(expected, result)

    def test_isfactorofall_2520_upto10_returnTrue(self):
        expected = True
        result = eular5.isfactorofall(2520, 10)
        self.assertEqual(expected, result)

    # Tests for num_div_by_all_upto(upto):
    def test_numdivbyallupto_1_returns1(self):
        expected = 1
        result = eular5.num_div_by_all_upto(1)
        self.assertEqual(expected, result)

    def test_numdivbyallupto_2_returns2(self):
        expected = 2
        result = eular5.num_div_by_all_upto(2)
        self.assertEqual(expected, result)

    def test_numdivbyallupto_3_returns6(self):
        expected = 6
        result = eular5.num_div_by_all_upto(3)
        self.assertEqual(expected, result)

    def test_numdivbyallupto_10_returns2520(self):
        expected = 2520
        result = eular5.num_div_by_all_upto(10)
        self.assertEqual(expected, result)
