import unittest
from GraphUnion import makeConnected  # Import the function from your script


class TestMakeConnected(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(makeConnected(4, [[0, 1], [0, 2], [1, 2]]), 1)

    def test_example2(self):
        self.assertEqual(makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]), 2)

    def test_example3(self):
        self.assertEqual(makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]]), -1)

    def test_fully_connected(self):
        self.assertEqual(makeConnected(3, [[0, 1], [1, 2], [0, 2]]), 0)

    def test_no_connections(self):
        self.assertEqual(makeConnected(5, []), -1)

    def test_single_computer(self):
        self.assertEqual(makeConnected(1, []), 0)

    def test_two_disconnected_computers(self):
        self.assertEqual(makeConnected(2, []), -1)

    def test_extra_cables(self):
        self.assertEqual(makeConnected(4, [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]), 0)


if __name__ == '__main__':
    unittest.main()
