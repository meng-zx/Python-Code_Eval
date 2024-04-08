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

# To run the tests
if __name__ == '__main__':
    unittest.main()
