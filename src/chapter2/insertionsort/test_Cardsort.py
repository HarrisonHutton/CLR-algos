import unittest
from cardsort import cardsort

class Test_Cardsort(unittest.TestCase):
    def test_empty(self):
        arr = []
        cardsort(arr)
        self.assertEqual(arr, [])


if __name__ == "__main__":
    unittest.main()
