import unittest
from src.jackw.main.searching import BinarySearch


class BinarySearchTest(unittest.TestCase):
    def test_search_value_found(self):
        test_array = [1, 5, 14, 89, 445, 564, 1123, 1234, 5641, 9999]
        index = BinarySearch.binary_search(test_array, 9999)
        self.assertEqual(index, 9)

    def test_search_value_not_found(self):
        test_array = [1, 5, 14, 89, 445, 564, 1123, 1234, 5641, 9999]
        index = BinarySearch.binary_search(test_array, 1010)
        self.assertEqual(index, -1)


if __name__ == '__main__':
    unittest.main()
