from ..src import eular_008


def test_calculateproduct_1_returns1():
    test_list = [1]
    result = eular_008.calculate_product(test_list)
    assert result == 1


def test_calculateproduct_1x2_returns2():
    test_list = [1, 2]
    result = eular_008.calculate_product(test_list)
    assert result == 2


def test_calculateproduct_1x2x3_returns6():
    test_list = [1, 2, 3]
    result = eular_008.calculate_product(test_list)
    assert result == 6


def test_calculateproduct_0x2x3_returns0():
    test_list = [0, 2, 3]
    result = eular_008.calculate_product(test_list)
    assert result == 0


def test_findproductinlist_1to9_3factors_returns504():
    factors = 3
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = eular_008.find_product_in_list(test_list, factors)
    assert result == 504


def test_findproductinlist_1to9_2factors_returns72():
    factors = 2
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = eular_008.find_product_in_list(test_list, factors)
    assert result == 72


def test_readfiletolist_just1_listIs1():
    result = eular_008.read_file_to_list('data/test_digits1.txt')
    assert result == [1]


def test_readfiletolist_3x3digits_listmatches():
    expected = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    result = eular_008.read_file_to_list('data/test_digits2.txt')
    assert result == expected
