import unittest
from insertionsort import insertionsort

class test_Insertionsort(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(insertionsort([]), [])


if __name__ == "__main__":
    unittest.main()
