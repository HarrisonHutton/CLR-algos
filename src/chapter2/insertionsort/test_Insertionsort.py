import unittest
from insertionsort import insertionsort

class test_Insertionsort(unittest.TestCase):
    def test_empty(self):
        arr = []
        insertionsort(arr)
        self.assertEqual(arr, [])

    def test_one_value(self):
        arr = [3]
        insertionsort(arr)
        self.assertEqual(arr, [3])

    def test_two_sorted_values(self):
        arr = [2,4]
        insertionsort(arr)
        self.assertEqual(arr, [2,4])

    def test_two_unsorted_values(self):
        arr = [5,1]
        insertionsort(arr)
        self.assertEqual(arr, [1,5])

    def test_three_sorted_values(self):
        arr = [1,5,76]
        insertionsort(arr)
        self.assertEqual(arr, [1,5,76])

    # Input will be partially sorted
    def test_three_unsorted_values(self):
        arr = [35,7,23]
        insertionsort(arr)
        self.assertEqual(arr, [7,23,35])


if __name__ == "__main__":
    unittest.main()
