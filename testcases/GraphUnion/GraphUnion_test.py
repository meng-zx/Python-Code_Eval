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

    def test_small_network(self):
        self.assertEqual(makeConnected(4, [[0, 1], [0, 2], [1, 2]]), 1)
        self.assertEqual(makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]), 2)
        self.assertEqual(makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]]), -1)

    def test_already_connected(self):
        self.assertEqual(makeConnected(3, [[0, 1], [1, 2]]), 0)

    def test_insufficient_cables(self):
        self.assertEqual(makeConnected(5, [[0, 1], [2, 3]]), -1)

    def test_large_network(self):
        # This test checks a large network with sufficient redundancy
        connections = [[i, i + 1] for i in range(99999)]
        self.assertEqual(makeConnected(100000, connections), 0)

    def test_no_computers(self):
        # Edge case with no computers
        self.assertEqual(makeConnected(1, []), 0)

    def test_two_computers_no_connection(self):
        # Two computers but no connection
        self.assertEqual(makeConnected(2, []), -1)

    def test_large_network_with_redundancies(self):
        # A large network where there are many redundant connections
        connections = [[i % 50000, (i + 1) % 50000] for i in range(100000)]
        self.assertEqual(makeConnected(50001, connections), 0)

    def test_large_network_insufficient_cables(self):
        # A large network with not enough cables to connect all computers
        connections = [[i, i + 1] for i in range(99998)]
        self.assertEqual(makeConnected(100000, connections), -1)

    def test_single_extra_cable_needed(self):
        # Exactly one extra cable is needed to connect all computers
        self.assertEqual(makeConnected(3, [[0, 1]]), 1)

    def test_network_fully_connected_no_extra_cables(self):
        # Network is already fully connected, no extra cables needed
        self.assertEqual(makeConnected(3, [[0, 1], [1, 2], [0, 2]]), 0)

    def test_large_network_fully_connected(self):
        # A large fully connected network
        connections = [[i, (i + 1) % 99999] for i in range(99999)]
        self.assertEqual(makeConnected(100000, connections), 0)

    def test_completely_disconnected(self):
        # All computers are disconnected
        self.assertEqual(makeConnected(5, []), -1)

    def test_two_components_need_two_cables(self):
        # Two separate components that need two cables to connect
        self.assertEqual(makeConnected(4, [[0, 1], [2, 3]]), -1)

    def test_complex_network_with_sufficient_cables(self):
        # A complex network with sufficient cables to make one additional connection
        self.assertEqual(makeConnected(5, [[0, 1], [1, 2], [3, 4]]), 1)

    def test_network_with_circular_connections(self):
        # A network forming a circle
        self.assertEqual(makeConnected(4, [[0, 1], [1, 2], [2, 3], [3, 0]]), 0)

    def test_network_with_one_way_connections_only(self):
        # A test case that mimics one-way connections, though in practice all connections are two-way
        self.assertEqual(makeConnected(4, [[0, 1], [1, 2], [2, 0]]), 1)

    def test_large_network_multiple_redundant_connections(self):
        # A large network with multiple redundant connections
        connections = [[0, 1], [1, 2], [2, 3]] + [[i, i + 4] for i in range(9996)]
        self.assertEqual(makeConnected(10000, connections), 0)

    def test_network_with_all_to_all_connections(self):
        # An overly connected network where every computer is connected to every other computer
        connections = [[i, j] for i in range(4) for j in range(i + 1, 4)]
        self.assertEqual(makeConnected(4, connections), 0)

    # ... Additional test cases can continue in this manner


if __name__ == '__main__':
    unittest.main()
