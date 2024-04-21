import unittest
from src.jackw.main.searching import LinearSearch


class LinearSearchTest(unittest.TestCase):
    def test_search_value_found(self):
        test_array = [1, 564, 1123, 9999, 5641, 1234, 5, 14, 89, 445]
        index = LinearSearch.linear_search(test_array, 9999)

        self.assertEqual(index, 3)

    def test_search_value_not_found(self):
        test_array = [1, 564, 1123, 9999, 5641, 1234, 5, 14, 89, 445]
        index = LinearSearch.linear_search(test_array, 1010)

        self.assertEqual(index, -1)


if __name__ == '__main__':
    unittest.main()
