import unittest
from TrappingRainWater import trap_water  # Import the function from your script

class TestWaterTrap(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(trap_water([0,1,0,2,1,0,1,3,2,1,2,1]), 6, "Should be 6 units of water")

    def test_example2(self):
        self.assertEqual(trap_water([4,2,0,3,2,5]), 9, "Should be 9 units of water")

    def test_empty(self):
        self.assertEqual(trap_water([]), 0, "Should be 0 units of water for empty list")

    def test_no_trap(self):
        self.assertEqual(trap_water([1,2,2,3,4]), 0, "Should be 0 units of water for increasing sequence")

    def test_single_peak(self):
        self.assertEqual(trap_water([3,0,3]), 3, "Should be 3 units of water for a single dip")

    def test_large_input(self):
        """Test with a very large input array"""
        large_input = [i % 3 for i in range(10000)]  # Repeating pattern
        self.assertIsInstance(trap_water(large_input), int, "Should handle large input efficiently")

    def test_empty(self):
        """Test with an empty array"""
        self.assertEqual(trap_water([]), 0, "Should be 0 for an empty list")

    def test_single_bar(self):
        """Test with a single bar"""
        self.assertEqual(trap_water([2]), 0, "Should be 0 for a single bar")

    def test_increasing_bars(self):
        """Test with strictly increasing bar heights"""
        self.assertEqual(trap_water([1, 2, 3, 4, 5]), 0, "Should be 0 for strictly increasing heights")

    def test_decreasing_bars(self):
        """Test with strictly decreasing bar heights"""
        self.assertEqual(trap_water([5, 4, 3, 2, 1]), 0, "Should be 0 for strictly decreasing heights")

    def test_large_numbers(self):
        """Test with very large numbers"""
        self.assertEqual(trap_water([100000, 1, 100000]), 99999, "Should be able to handle large numbers")

    def test_alternating_high_low(self):
        """Test with alternating high and low bars"""
        self.assertEqual(trap_water([2, 0, 2, 0, 2]), 4, "Should work for alternating high and low bars")

    def test_flat_surface(self):
        """Test with a flat surface"""
        self.assertEqual(trap_water([1, 1, 1, 1]), 0, "Should be 0 for flat surfaces")

    def test_single_dip(self):
        """Test with a single dip"""
        self.assertEqual(trap_water([3, 1, 2]), 1, "Should handle a single dip correctly")

    def test_peak_at_start(self):
        """Test with a peak at the start"""
        self.assertEqual(trap_water([4, 1, 2, 3]), 3, "Should handle a peak at the start")

    def test_peak_at_end(self):
        """Test with a peak at the end"""
        self.assertEqual(trap_water([1, 2, 3, 4]), 0, "Should handle a peak at the end correctly")

    def test_random_distribution(self):
        """Test with a random distribution of heights"""
        self.assertEqual(trap_water([3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3]), 9, "Should handle random distributions")

    def test_repeated_patterns(self):
        """Test with repeated patterns"""
        self.assertEqual(trap_water([2, 1, 2, 1, 2, 1, 2]), 3, "Should work for repeated patterns")

    def test_all_same_height(self):
        """Test with all bars having the same height"""
        self.assertEqual(trap_water([3, 3, 3, 3]), 0, "Should be 0 for bars of the same height")

    def test_descending_then_ascending(self):
        """Test with heights descending then ascending"""
        self.assertEqual(trap_water([5, 4, 3, 4, 5]), 2, "Should trap water in a valley")

    def test_peak_in_the_middle(self):
        """Test with a peak in the middle"""
        self.assertEqual(trap_water([1, 2, 4, 2, 1]), 0, "No water should be trapped with a central peak")

    def test_dips_on_edges(self):
        """Test with dips on both edges"""
        self.assertEqual(trap_water([1, 3, 2, 4, 2, 3, 1]), 2, "Should handle dips on both edges")

    def test_high_plateau(self):
        """Test with a high plateau"""
        self.assertEqual(trap_water([1, 2, 5, 5, 5, 2, 1]), 0, "No water should be trapped on a plateau")

    def test_low_plateau_in_middle(self):
        """Test with a low plateau in the middle"""
        self.assertEqual(trap_water([3, 2, 1, 1, 1, 2, 3]), 6, "Should trap water on a surrounded plateau")

    def test_sawtooth_pattern(self):
        """Test with a sawtooth pattern"""
        self.assertEqual(trap_water([1, 0, 1, 0, 1, 0, 1]), 3, "Should trap water in a sawtooth pattern")

    def test_large_input_ascending_descending(self):
        """Test with a large input array, ascending then descending"""
        large_input = list(range(1000)) + list(range(1000, 0, -1))
        self.assertEqual(trap_water(large_input), 0, "Should be 0 for a mountain shape")

    def test_single_large_dip(self):
        """Test with a single large dip"""
        self.assertEqual(trap_water([10, 1, 10]), 9, "Should trap a significant amount of water in a large dip")

    def test_complex_pattern(self):
        """Test with a complex pattern of bars"""
        complex_pattern = [5, 1, 4, 2, 3, 1, 4, 5]
        self.assertEqual(trap_water(complex_pattern), 9, "Should handle complex patterns correctly")

    def test_increasing_decreasing_with_plateau(self):
        """Test with increasing, plateau, and then decreasing heights"""
        self.assertEqual(trap_water([1, 2, 2, 2, 1]), 0, "Should handle plateaus correctly")

    def test_large_numbers_random(self):
        """Test with large numbers in a random pattern"""
        large_random = [100, 1, 500, 200, 100, 400, 300]
        self.assertEqual(trap_water(large_random), 299, "Should work with large random numbers")

    def test_long_plateau(self):
        """Test with a long, flat plateau"""
        self.assertEqual(trap_water([2, 2, 2, 2]), 0, "Should be 0 for a long plateau")

    def test_very_deep_single_dip(self):
        """Test with a very deep, single dip"""
        self.assertEqual(trap_water([100, 0, 100]), 100, "Should trap a very large amount of water in a deep dip")

    def test_multiple_peaks_and_valleys(self):
        """Test with multiple peaks and valleys"""
        self.assertEqual(trap_water([2, 1, 2, 1, 2, 1, 2, 3]), 4, "Should work for multiple peaks and valleys")

    def test_ascending_plateau_descending(self):
        """Test with an ascending plateau then descending"""
        self.assertEqual(trap_water([1, 2, 2, 2, 3, 2, 1]), 1, "Should handle ascending plateau then descending")

    def test_large_input_with_zeros(self):
        """Test with a large input array containing zeros"""
        large_with_zeros = [0] * 10000 + [1] + [0] * 10000
        self.assertEqual(trap_water(large_with_zeros), 0, "Should be 0 for large arrays with zeros")

    def test_sharp_peak(self):
        """Test with a sharp peak"""
        self.assertEqual(trap_water([1, 100, 1]), 0, "No water should be trapped by a sharp peak")

    def test_wide_valley(self):
        """Test with a wide valley"""
        self.assertEqual(trap_water([3, 1, 1, 1, 1, 3]), 8, "Should trap water in a wide valley")

    def test_rapid_altitude_changes(self):
        """Test with rapid altitude changes"""
        self.assertEqual(trap_water([5, 4, 3, 4, 5, 2, 1, 2, 3]), 4, "Should handle rapid altitude changes")


# To run the tests
if __name__ == '__main__':
    unittest.main()
