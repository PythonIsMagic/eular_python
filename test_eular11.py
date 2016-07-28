import unittest
import eular11


class TestEular11(unittest.TestCase):
    # Tests for read_file_to_matrix(filename):
    # Reading just 0 in a file, returns 1x1 matrix with 0
    def test_readmatrix_1x1file_1x1matrix(self):
        expected = [[0]]
        result = eular11.read_matrix('test_matrix1.txt')
        self.assertEqual(expected, result)

    def test_readmatrix_2x2file_zerofilled_2x2matrix(self):
        expected = [[1, 2], [3, 4]]
        result = eular11.read_matrix('test_matrix2.txt')
        self.assertEqual(expected, result)

    def test_readmatrix_2x2file_nonfilled_2x2matrix(self):
        expected = [[1, 2], [3, 4]]
        result = eular11.read_matrix('test_matrix3.txt')
        self.assertEqual(expected, result)

    def test_readmatrix_3x3file_zerofilled_3x3matrix(self):
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = eular11.read_matrix('test_matrix4.txt')
        self.assertEqual(expected, result)

    # Tests for print_matrix(matrix):
    def test_printmatrix_1x1(self):
        expected = '00\n'
        matrix = eular11.read_matrix('test_matrix1.txt')
        result = eular11.print_matrix(matrix)
        self.assertEqual(expected, result)

    def test_printmatrix_2x2file_zerofilled(self):
        expected = '01 02\n03 04\n'
        matrix = eular11.read_matrix('test_matrix2.txt')
        result = eular11.print_matrix(matrix)
        self.assertEqual(expected, result)

    def test_printmatrix_2x2file_nonfilled(self):
        expected = '01 02\n03 04\n'
        matrix = eular11.read_matrix('test_matrix3.txt')
        result = eular11.print_matrix(matrix)
        self.assertEqual(expected, result)

    # Tests get_rows(matrix):
    def test_getrows_3x3_returns3lists(self):
        expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        m = eular11.read_matrix('test_matrix4.txt')
        result = eular11.get_rows(m)
        self.assertEqual(expected, result)

    # Tests get_columns(matrix):
    def test_getcolumns_3x3_returns3lists(self):
        expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        m = eular11.read_matrix('test_matrix4.txt')
        result = eular11.get_columns(m)
        self.assertEqual(expected, result)

    # Tests get_right_diagonals(matrix):
    def test_get_right_diagonals_3x3_returns5lists(self):
        expected = [[7], [4, 8], [1, 5, 9], [2, 6], [3]]
        m = eular11.read_matrix('test_matrix4.txt')
        result = eular11.get_right_diagonals(m)
        self.assertEqual(expected, result)

    # Tests get_left_diagonals(matrix):
    def test_get_left_diagonals_3x3_returns5lists(self):
        expected = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
        m = eular11.read_matrix('test_matrix4.txt')
        result = eular11.get_left_diagonals(m)
        self.assertEqual(expected, result)

    # Tests for find_greatest_product(factors)
    def test_findgreatestproduct_3x3_returns504(self):
        # 7 * 8 * 9 = 504
        expected = 504
        m = eular11.read_matrix('test_matrix4.txt')
        result = eular11.find_greatest_product(m, 3)
        self.assertEqual(expected, result)

    # Tests for find_greatest_product(factors)
    def test_findgreatestproduct_2x2_returns12(self):
        expected = 12
        m = eular11.read_matrix('test_matrix2.txt')
        result = eular11.find_greatest_product(m, 2)
        self.assertEqual(expected, result)
