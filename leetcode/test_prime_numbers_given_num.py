import unittest
from find_prime_numbers_given_num import is_prime

class TestPrimeNumbersGivenNum(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(7))
    def test_not_prime(self):
        self.assertFalse(is_prime(6))


if __name__ == "__main__":
    unittest.main()