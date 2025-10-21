import unittest
from check_anagram import check_anagrams

class TestCheckAnagramChecker(unittest.TestCase):
    def test_are_anagram(self):
        self.assertEqual(check_anagrams("vijay","jayvi"), "Strings are Anagram")
    def test_are_not_anagram(self):
        self.assertEqual(check_anagrams("racecar","carace"), "Strings are not Anagram")

if __name__ == "__main__":
    unittest.main()