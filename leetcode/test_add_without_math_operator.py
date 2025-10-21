import unittest
from add_without_math_operator import add


class Test_Add_Without_Math_Operator(unittest.TestCase):
    def test_correct_output(self):
        result=add(7,2)
        print("Result of add(7, 2):", result)
        self.assertEqual(result, 9)
    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            add("int", 2) 
    def test_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)
        self.assertEqual(add(-5, 3), -2)
    def test_incorrect_sum(self):
        self.assertNotEqual(add(5, 5), 11)



if __name__ == "__main__":
    unittest.main()