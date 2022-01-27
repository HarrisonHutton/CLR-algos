import unittest
from insertionsort import insertionsort

class test_Insertionsort(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(insertionsort([]), [])

    def test_one_value(self):
        self.assertEqual(insertionsort([3]), [3])

    def test_two_sorted_values(self):
        self.assertEqual(insertionsort([2,4]), [2,4])

    def test_two_unsorted_values(self):
        self.assertEqual(insertionsort([5,1]), [1,5])

    def test_three_sorted_values(self):
        self.assertEqual(insertionsort([1,5,76]), [1,5,76])

    # Input will be partially sorted
    def test_three_unsorted_values(self):
        self.assertEqual(insertionsort([35,7,23]), [7,23,35])


if __name__ == "__main__":
    unittest.main()
