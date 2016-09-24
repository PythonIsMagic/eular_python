import unittest
import functions


class TestFunctions(unittest.TestCase):
    def test_ismultipleof_emptylist_returnFalse(self):
        expected = False
        result = functions.is_multiple_of(10, [])
        self.assertEqual(expected, result)

    def test_ismultipleof_1div1_ReturnTrue(self):
        expected = True
        result = functions.is_multiple_of(1, [1])
        self.assertEqual(expected, result)

    def test_ismultipleof_0div1_ReturnTrue(self):
        expected = True
        result = functions.is_multiple_of(0, [1])
        self.assertEqual(expected, result)

    def test_ismultipleof_1div0_RaiseException(self):
        self.assertRaises(ValueError, functions.is_multiple_of, 1, [0])

        #  expected = False
        #  result = functions.is_multiple_of(1, [0])
        #  self.assertEqual(expected, result)

    def test_ismultipleof_1div2_ReturnFalse(self):
        expected = False
        result = functions.is_multiple_of(1, [2])
        self.assertEqual(expected, result)

    def test_ismultipleof_4div2_ReturnTrue(self):
        expected = True
        result = functions.is_multiple_of(4, [2])
        self.assertEqual(expected, result)

    def test_ismultipleof_3fromlist_ReturnTrue(self):
        expected = True
        result = functions.is_multiple_of(3, [1, 2, 9])
        self.assertEqual(expected, result)
