import unittest
import multiprocessing
from find_duplicate_string import find_duplicate

class TestFindDuplicates(unittest.TestCase):
    def test_find_duplicate(self):
        self.assertEqual(find_duplicate(["vishal", "ramesh", "vijay", "vishal", "latha"]), ["vishal"])

    def test_no_elements_found(self):
        self.assertEqual(find_duplicate(["vishal", "ramesh", "vijay", "latha"]), "No duplicates found")

    def test_empty_list(self):
        self.assertEqual(find_duplicate([]), "No duplicates found")

    def test_all_duplicates(self):
        self.assertEqual(find_duplicate(["a", "a", "a", "a"]), ["a"])

    def test_multiple_duplicates(self):
        self.assertEqual(find_duplicate(["apple", "banana", "apple", "banana", "cherry", "banana"]), ["apple", "banana"])

    def test_case_sensitivity(self):
        self.assertEqual(find_duplicate(["Apple", "apple", "APPLE"]), "No duplicates found")

    def test_special_characters(self):
        self.assertEqual(find_duplicate(["@data", "#data", "@data", "#info"]), ["@data"])


if __name__ == "__main__":
    with multiprocessing.Pool(7) as pool:
        unittest.main()