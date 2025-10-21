import unittest
from count_only_caps import count_char

class Test_Count_Only_caps(unittest.TestCase):
    def test_add_caps(self):
        result=count_char("InDiA")
        self.assertEqual(result,3)
        print("Count of UC Char is : ", result)

if __name__ == "__main__":
    unittest.main()