import unittest
from sorter import sort

class TestSorter(unittest.TestCase):

    def test_standard(self):
        self.assertEqual(sort(10, 10, 10, 5), "STANDARD")

    def test_bulky_by_volume(self):
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")

    def test_bulky_by_dimension(self):
        self.assertEqual(sort(150, 10, 10, 5), "SPECIAL")

    def test_heavy(self):
        self.assertEqual(sort(10, 10, 10, 20), "SPECIAL")

    def test_rejected(self):
        self.assertEqual(sort(150, 100, 100, 25), "REJECTED")

    def test_edge_case_exact_limits(self):
        self.assertEqual(sort(100, 100, 100, 20), "REJECTED")

if __name__ == "__main__":
    unittest.main()
