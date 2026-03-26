import unittest

class MathTools:
    def square(self, n):
        return n * n

    def cube(self, n):
        return n * n * n

class TestMathTools(unittest.TestCase):

    def setUp(self):
        # This method runs before each test
        self.math = MathTools()

    def test_square(self):
        self.assertEqual(self.math.square(2), 4)
        self.assertEqual(self.math.square(-3), 9)

    def test_cube(self):
        self.assertEqual(self.math.cube(2), 8)
        self.assertEqual(self.math.cube(-2), -8)


if __name__ == '__main__':
    unittest.main()