import unittest
import eular11
import matrix


class TestEular11(unittest.TestCase):
    # Tests for find_greatest_product(factors)
    def test_findgreatestproduct_3x3_returns504(self):
        # 7 * 8 * 9 = 504
        expected = 504
        m = matrix.read_matrix('test_matrix4.txt')
        result = eular11.find_greatest_product(m, 3)
        self.assertEqual(expected, result)

    # Tests for find_greatest_product(factors)
    def test_findgreatestproduct_2x2_returns12(self):
        expected = 12
        m = matrix.read_matrix('test_matrix2.txt')
        result = eular11.find_greatest_product(m, 2)
        self.assertEqual(expected, result)
