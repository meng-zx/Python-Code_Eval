import unittest
from MedianSortedArray import findMedianSortedArrays  # Import the function from your script

class TestFindMedianSortedArrays(unittest.TestCase):
    def test_example1(self):
        nums1 = [1, 3]
        nums2 = [2]
        expected = 2.0
        self.assertEqual(findMedianSortedArrays(nums1, nums2), expected)

    def test_example2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        expected = 2.5
        self.assertEqual(findMedianSortedArrays(nums1, nums2), expected)

    def test_empty_first_array(self):
        nums1 = []
        nums2 = [1]
        expected = 1.0
        self.assertEqual(findMedianSortedArrays(nums1, nums2), expected)

    def test_empty_second_array(self):
        nums1 = [2]
        nums2 = []
        expected = 2.0
        self.assertEqual(findMedianSortedArrays(nums1, nums2), expected)

    def test_both_empty_arrays(self):
        nums1 = []
        nums2 = []
        self.assertRaises(ValueError, findMedianSortedArrays, nums1, nums2)

    def test_large_numbers(self):
        nums1 = [100000]
        nums2 = [100001]
        expected = 100000.5
        self.assertEqual(findMedianSortedArrays(nums1, nums2), expected)

if __name__ == '__main__':
    unittest.main()
