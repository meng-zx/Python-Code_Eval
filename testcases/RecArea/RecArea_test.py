import unittest
from RecArea import compute_area  # Import the function from your scriptimport unittest

class TestComputeArea(unittest.TestCase):
    def test_overlap(self):
        self.assertEqual(compute_area(-3, 0, 3, 4, 0, -1, 9, 2), 45)

    def test_complete_overlap(self):
        self.assertEqual(compute_area(-2, -2, 2, 2, -2, -2, 2, 2), 16)

    def test_no_overlap(self):
        self.assertEqual(compute_area(-3, 0, 3, 4, 4, 5, 5, 6), 9)


    def test_touching_rectangles(self):
        self.assertEqual(compute_area(-3, 0, 3, 4, 3, 0, 6, 4), 42)

    def test_overlapping_lines(self):
        self.assertEqual(compute_area(-3, 0, 3, 0, -1, 0, 2, 0), 0)

    def test_one_line_rectangle(self):
        self.assertEqual(compute_area(-3, 0, 3, 0, 0, -1, 9, 2), 15)

    def test_large_coordinates(self):
        self.assertEqual(compute_area(-10000, -10000, 10000, 10000, -10000, -10000, 10000, 10000), 400000000)

    def test_no_overlap_large_coordinates(self):
        self.assertEqual(compute_area(-10000, -10000, -5000, -5000, 5000, 5000, 10000, 10000), 50000000)

    def test_large_negative_coordinates(self):
        self.assertEqual(compute_area(-10000, -10000, -9000, -9000, -9500, -9500, -8500, -8500), 25000000)

    def test_rectangles_with_zero_width(self):
        self.assertEqual(compute_area(-3, 0, -3, 4, 0, 0, 0, 5), 0)

    def test_rectangles_with_zero_height(self):
        self.assertEqual(compute_area(-3, 4, 3, 4, -1, 2, 2, 2), 0)


    def test_both_rectangles_as_points(self):
        self.assertEqual(compute_area(1, 1, 1, 1, 2, 2, 2, 2), 0)

    def test_overlap_with_negative_and_positive_quadrants(self):
        self.assertEqual(compute_area(-3, -3, 3, 3, -2, -2, 2, 2), 36)

    def test_large_rectangle_with_small_overlap(self):
        self.assertEqual(compute_area(-10000, -10000, 10000, 10000, -1, -1, 1, 1), 400000004)

    def test_small_rectangle_fully_inside_large_rectangle(self):
        self.assertEqual(compute_area(-100, -100, 100, 100, -1, -1, 1, 1), 40000)

    def test_extremely_small_overlap(self):
        self.assertEqual(compute_area(-100, -100, 100, 100, 99, 99, 101, 101), 40004)

    def test_rectangles_touching_sides_not_overlapping(self):
        self.assertEqual(compute_area(-4, -4, 0, 0, 0, 0, 4, 4), 32)

    def test_overlapping_edges_exactly(self):
        self.assertEqual(compute_area(-10, -10, -5, 0, -5, -10, 0, 0), 100)


if __name__ == '__main__':
    unittest.main()
