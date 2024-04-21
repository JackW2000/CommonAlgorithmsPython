import unittest
from src.jackw.main.sorting import HeapSort


class HeapSortTest(unittest.TestCase):
    def test_sort_unordered_array(self):
        unsorted_arr = [1, 564, 1123, 9999, 5641, 1234, 5, 14, 89, 445]
        sorted_arr = [1, 5, 14, 89, 445, 564, 1123, 1234, 5641, 9999]
        HeapSort.heap_sort(unsorted_arr)
        self.assertEqual(unsorted_arr, sorted_arr)


if __name__ == '__main__':
    unittest.main()
