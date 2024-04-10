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


    def test_already_connected(self):
        self.assertEqual(makeConnected(3, [[0, 1], [1, 2]]), 0)

    def test_insufficient_cables(self):
        self.assertEqual(makeConnected(5, [[0, 1], [2, 3]]), -1)



    def test_no_computers(self):
        # Edge case with no computers
        self.assertEqual(makeConnected(1, []), 0)

    def test_two_computers_no_connection(self):
        # Two computers but no connection
        self.assertEqual(makeConnected(2, []), -1)



    def test_single_extra_cable_needed(self):
        # Exactly one extra cable is needed to connect all computers
        self.assertEqual(makeConnected(3, [[0, 1]]), 1)

    def test_network_fully_connected_no_extra_cables(self):
        # Network is already fully connected, no extra cables needed
        self.assertEqual(makeConnected(3, [[0, 1], [1, 2], [0, 2]]), 0)


    def test_completely_disconnected(self):
        # All computers are disconnected
        self.assertEqual(makeConnected(5, []), -1)

    def test_two_components_need_two_cables(self):
        # Two separate components that need two cables to connect
        self.assertEqual(makeConnected(4, [[0, 1], [2, 3]]), -1)



    def test_large_network_multiple_redundant_connections(self):
        # A large network with multiple redundant connections
        connections = [[0, 1], [1, 2], [2, 3]] + [[i, i + 4] for i in range(96)]
        self.assertEqual(makeConnected(100, connections), 0)


    # ... Additional test cases can continue in this manner


if __name__ == '__main__':
    unittest.main()
