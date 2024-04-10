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

    def test_empty_arrays(self):
        def test_one_empty_array(self):
            self.assertEqual(findMedianSortedArrays([1, 3], []), 2)



        def test_odd_length(self):
            self.assertEqual(findMedianSortedArrays([1, 3], [2]), 2)

        def test_uneven_length(self):
            self.assertEqual(findMedianSortedArrays([1, 2], [3, 4, 5]), 3)

        def test_all_same_value(self):
            self.assertEqual(findMedianSortedArrays([1, 1, 1], [1, 1, 1]), 1)

        def test_reversed_arrays(self):
            self.assertEqual(findMedianSortedArrays([3, 2, 1], [4, 3, 2]), 2.5)

        def test_max_array_lengths(self):
            self.assertEqual(findMedianSortedArrays([1] * 1000, [2] * 1000), 1.5)

        def test_negative_values(self):
            self.assertEqual(findMedianSortedArrays([-1, 3], [-2, 2]), 0.5)


if __name__ == '__main__':
    unittest.main()
