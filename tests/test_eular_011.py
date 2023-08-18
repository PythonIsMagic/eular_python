import pytest

from ..src import eular_011

# Tests for extract_line(matrix, point, xyincrement) are implicit since get_rows,
# get_columns, get_right_diagonals, get_right_diagonals use extract_line.


def test_readmatrix_1x1file_1x1matrix():
    expected = [[0]]
    result = eular_011.read_matrix('data/test_matrix1.txt')
    assert result == expected


def test_readmatrix_2x2file_zerofilled_2x2matrix():
    expected = [[1, 2], [3, 4]]
    result = eular_011.read_matrix('data/test_matrix2.txt')
    assert result == expected


def test_readmatrix_2x2file_nonfilled_2x2matrix():
    expected = [[1, 2], [3, 4]]
    result = eular_011.read_matrix('data/test_matrix3.txt')
    assert result == expected


def test_readmatrix_3x3file_zerofilled_3x3matrix():
    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = eular_011.read_matrix('data/test_matrix4.txt')
    assert result == expected


def test_printmatrix_1x1():
    expected = '00\n'
    m = eular_011.read_matrix('data/test_matrix1.txt')
    result = eular_011.print_matrix(m)
    assert result == expected


def test_printmatrix_2x2file_zerofilled():
    expected = '01 02\n03 04\n'
    m = eular_011.read_matrix('data/test_matrix2.txt')
    result = eular_011.print_matrix(m)
    assert result == expected


def test_printmatrix_2x2file_nonfilled():
    expected = '01 02\n03 04\n'
    m = eular_011.read_matrix('data/test_matrix3.txt')
    result = eular_011.print_matrix(m)
    assert result == expected


def test_getrows_3x3_returns3lists():
    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m = eular_011.read_matrix('data/test_matrix4.txt')
    result = eular_011.get_rows(m)
    assert result == expected


def test_getcolumns_3x3_returns3lists():
    expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    m = eular_011.read_matrix('data/test_matrix4.txt')
    result = eular_011.get_columns(m)
    assert result == expected


def test_get_right_diagonals_3x3_returns5lists():
    expected = [[7], [4, 8], [1, 5, 9], [2, 6], [3]]
    m = eular_011.read_matrix('data/test_matrix4.txt')
    result = eular_011.get_right_diagonals(m)
    assert result == expected


def test_get_left_diagonals_3x3_returns5lists():
    expected = [[1], [2, 4], [3, 5, 7], [6, 8], [9]]
    m = eular_011.read_matrix('data/test_matrix4.txt')
    result = eular_011.get_left_diagonals(m)
    assert result == expected


def test_scanmatrixlines_3x3_returns16lists():
    """ Make sure we get all the right lines from the matrix.
        In this order: rows, columns, right diagonals, left diagonals.
    """
    expected = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [7], [4, 8], [1, 5, 9], [2, 6], [3],
        [1], [2, 4], [3, 5, 7], [6, 8], [9]
    ]
    m = eular_011.read_matrix('data/test_matrix4.txt')
    result = eular_011.scan_matrix_lines(m)
    assert result == expected


def test_findgreatestproduct_3x3_returns504():
    # 7 * 8 * 9 = 504
    m = eular_011.read_matrix('data/test_matrix4.txt')
    result = eular_011.find_greatest_product(m, 3)
    assert result == 504


def test_findgreatestproduct_2x2_returns12():
    m = eular_011.read_matrix('data/test_matrix2.txt')
    result = eular_011.find_greatest_product(m, 2)
    assert result == 12


def test_multiply_2factors_returns2():
    n = [1, 2, 3, 4, 5]
    result = eular_011.multiply(n, 0, 2)
    assert result == 2


def test_multiply_3factors_returns6():
    n = [1, 2, 3, 4, 5]
    result = eular_011.multiply(n, 0, 3)
    assert result == 6


def test_multiply_3factors_index1_returns24():
    n = [1, 2, 3, 4, 5]
    result = eular_011.multiply(n, 1, 3)
    assert result == 24


def test_multiply_indexoutofbounds_raiseException():
    n = [1, 2, 3, 4, 5]
    with pytest.raises(ValueError):
        eular_011.multiply(n, 10, 3)


def test_multiply_3factors_size3_returns24():
    n = [2, 3, 4]
    result = eular_011.multiply(n, 0, 3)
    assert result == 24


def test_multiply_13factors_size14_index0_returns157689344584365834240():
    n = [32, 26, 58, 9, 22, 35, 89, 69, 7, 46, 72, 69, 48, 43]
    expected = 157689344584365834240
    result = eular_011.multiply(n, 0, 13)
    assert result == expected


def test_multiply_13factors_size14_index1_returns211895056785241589760():
    n = [32, 26, 58, 9, 22, 35, 89, 69, 7, 46, 72, 69, 48, 43]
    expected = 211895056785241589760
    result = eular_011.multiply(n, 1, 13)
    assert result == expected
