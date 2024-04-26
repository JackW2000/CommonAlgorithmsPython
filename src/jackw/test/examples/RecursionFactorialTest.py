import unittest

from src.jackw.main.examples.RecursionFactorial import factorial


class RecursionFactorialTest(unittest.TestCase):
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial(self):
        self.assertEqual(factorial(10), 3628800)


if __name__ == '__main__':
    unittest.main()
