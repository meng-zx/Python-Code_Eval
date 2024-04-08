import unittest
from TwoSum import two_sum

class TestTwoSum(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(sorted(two_sum([2, 7, 11, 15], 9)), [0, 1])
    
    def test_example2(self):
        self.assertEqual(sorted(two_sum([3, 2, 4], 6)), [1, 2])
    
    def test_example3(self):
        self.assertEqual(sorted(two_sum([3, 3], 6)), [0, 1])
    
    def test_negative_numbers(self):
        self.assertEqual(sorted(two_sum([-3, 4, 3, 90], 0)), [0, 2])
    
    def test_large_numbers(self):
        self.assertEqual(sorted(two_sum([123456789, -123456788], 1)), [0, 1])

if __name__ == '__main__':
    unittest.main()
