import unittest
from RecArea import compute_area  # Import the function from your scriptimport unittest

class TestComputeArea(unittest.TestCase):
    def test_overlap(self):
        self.assertEqual(compute_area(-3, 0, 3, 4, 0, -1, 9, 2), 45)

    def test_complete_overlap(self):
        self.assertEqual(compute_area(-2, -2, 2, 2, -2, -2, 2, 2), 16)

    def test_no_overlap(self):
        self.assertEqual(compute_area(-3, 0, 3, 4, 4, 5, 5, 6), 9)

    def test_contained(self):
        self.assertEqual(compute_area(-4, -4, 4, 4, -2, -2, 2, 2), 64)

    def test_edge_touching(self):
        self.assertEqual(compute_area(-2, -2, 2, 2, 2, -2, 4, 2), 16)

    def test_corner_touching(self):
        self.assertEqual(compute_area(-2, -2, 0, 0, 0, 0, 2, 2), 8)

    def test_negative_coordinates(self):
        self.assertEqual(compute_area(-4, -4, -2, -2, -3, -3, -1, -1), 9)

if __name__ == '__main__':
    unittest.main()
