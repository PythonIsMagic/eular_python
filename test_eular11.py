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

    # Tests for horizontal_product(alist, index, factors):
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    def test_horzprod_0_1_returns0(self):
        items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = 0
        result = eular11.horz_prod(items, 0, 2)
        self.assertEqual(expected, result)

    # Tests for get_product(alist, index, factors):

