import unittest
from check_palindrome import is_palindrome

class TestPalindromeChecker(unittest.TestCase):
    def test_palindrome_number(self):
        self.assertEqual(is_palindrome(121), "is palindrome")
        self.assertEqual(is_palindrome(12321), "is palindrome")

    def test_non_palindrome_number(self):
        self.assertEqual(is_palindrome(123), "not palindrome")
        self.assertEqual(is_palindrome(10), "not palindrome")

    def test_zero_and_negative(self):
        self.assertEqual(is_palindrome(0), "Number should be greater than 0")
        self.assertEqual(is_palindrome(-121), "Number should be greater than 0")

if __name__ == "__main__":
    unittest.main()