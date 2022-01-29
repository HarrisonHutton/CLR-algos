import unittest
from insertionsort_v2 import bwardsinsertionsort

class test_Insertionsort(unittest.TestCase):
    def test_empty(self):
        arr = []
        bwardsinsertionsort(arr)
        self.assertEqual(arr, [])

    def test_one_value(self):
        arr = [3]
        bwardsinsertionsort(arr)
        self.assertEqual(arr, [3])

    def test_two_unsorted_values(self):
        arr = [2,4]
        bwardsinsertionsort(arr)
        self.assertEqual(arr, [4,2])

    def test_two_sorted_values(self):
        arr = [5,1]
        bwardsinsertionsort(arr)
        self.assertEqual(arr, [5,1])

    def test_three_unsorted_values(self):
        arr = [1,5,76]
        bwardsinsertionsort(arr)
        self.assertEqual(arr, [76,5,1])

    # Input will be partially sorted
    def test_three_partially_unsorted_values(self):
        arr = [35,7,23]
        bwardsinsertionsort(arr)
        self.assertEqual(arr, [35,23,7])

    def test_three_sorted_values(self):
        arr = [5,5,4]
        bwardsinsertionsort(arr)
        self.assertEqual(arr, [5,5,4])


if __name__ == "__main__":
    unittest.main()
