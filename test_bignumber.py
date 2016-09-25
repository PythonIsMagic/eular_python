import unittest
import bignumber


class TestBigNumber(unittest.TestCase):
    # Tests for sum_of_squares(upto):

    # Tests for read_file_to_list(filename)
    def test_readfiletolist_just1_listIs1(self):
        expected = [1]
        result = bignumber.read_file_to_list('test_digits1.txt')
        self.assertEqual(expected, result)

    def test_readfiletolist_3x3digits_listmatches(self):
        expected = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        result = bignumber.read_file_to_list('test_digits2.txt')
        self.assertEqual(expected, result)

    # Tests for calculate_product(alist)
    def test_calculateproduct_1_returns1(self):
        expected = 1
        test_list = [1]
        result = bignumber.calculate_product(test_list)
        self.assertEqual(expected, result)

    def test_calculateproduct_1x2_returns2(self):
        expected = 2
        test_list = [1, 2]
        result = bignumber.calculate_product(test_list)
        self.assertEqual(expected, result)

    def test_calculateproduct_1x2x3_returns6(self):
        expected = 6
        test_list = [1, 2, 3]
        result = bignumber.calculate_product(test_list)
        self.assertEqual(expected, result)

    def test_calculateproduct_0x2x3_returns0(self):
        expected = 0
        test_list = [0, 2, 3]
        result = bignumber.calculate_product(test_list)
        self.assertEqual(expected, result)

    # Tests for find_product_in_list(alist, factors)
    def test_findproductinlist_1to9_3factors_returns504(self):
        factors = 3
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = 504
        result = bignumber.find_product_in_list(test_list, factors)
        self.assertEqual(expected, result)

    def test_findproductinlist_1to9_2factors_returns72(self):
        factors = 2
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = 72
        result = bignumber.find_product_in_list(test_list, factors)
        self.assertEqual(expected, result)
