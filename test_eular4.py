import unittest
import eular4


class TestEular4(unittest.TestCase):
    # Tests for ispalindrome(number):
    def test_ispalindrome_emptyString_returnFalse(self):
        expected = False
        result = eular4.ispalindrome('')
        self.assertEqual(expected, result)

    def test_ispalindrome_1_returnTrue(self):
        expected = True
        result = eular4.ispalindrome(1)
        self.assertEqual(expected, result)

    def test_ispalindrome_10_returnFalse(self):
        expected = False
        result = eular4.ispalindrome(10)
        self.assertEqual(expected, result)

    def test_ispalindrome_11_returnTrue(self):
        expected = True
        result = eular4.ispalindrome(11)
        self.assertEqual(expected, result)

    def test_ispalindrome_101_returnTrue(self):
        expected = True
        result = eular4.ispalindrome(101)
        self.assertEqual(expected, result)

    def test_ispalindrome_110_returnFalse(self):
        expected = False
        result = eular4.ispalindrome(110)
        self.assertEqual(expected, result)


    # Tests for get_largest_palindrome(lowerlimit, upperlimit):
    def test_getlargestpalindrome_2digit_returns9009(self):
        expected = 9009
        result = eular4.get_largest_palindrome(10, 100)
        self.assertEqual(expected, result)
