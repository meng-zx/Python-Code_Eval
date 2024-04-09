import unittest
from LIS import lengthOfLIS  # Import the function from your script

class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_example_cases(self):
        # Test case 1
        self.assertEqual(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4, "Example 1 failed")
        # Test case 2
        self.assertEqual(lengthOfLIS([0, 1, 0, 3, 2, 3]), 4, "Example 2 failed")
        # Test case 3
        self.assertEqual(lengthOfLIS([7, 7, 7, 7, 7, 7, 7]), 1, "Example 3 failed")

    def test_edge_cases(self):
        # Empty array
        self.assertEqual(lengthOfLIS([]), 0, "Empty array test failed")
        # Single element
        self.assertEqual(lengthOfLIS([10]), 1, "Single element test failed")
        # Decreasing sequence
        self.assertEqual(lengthOfLIS([5, 4, 3, 2, 1]), 1, "Decreasing sequence test failed")
        # Increasing sequence
        self.assertEqual(lengthOfLIS([1, 2, 3, 4, 5]), 5, "Increasing sequence test failed")
        # All elements are the same
        self.assertEqual(lengthOfLIS([2, 2, 2, 2]), 1, "All elements same test failed")

if __name__ == "__main__":
    unittest.main()
