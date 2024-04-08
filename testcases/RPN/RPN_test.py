import unittest
from RPN import evalRPN  # Import the function from your script

class TestEvalRPN(unittest.TestCase):

    def test_example1(self):
        self.assertEqual(evalRPN(["2", "1", "+", "3", "*"]), 9)

    def test_example2(self):
        self.assertEqual(evalRPN(["4", "13", "5", "/", "+"]), 6)

    def test_example3(self):
        self.assertEqual(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)

    def test_division(self):
        self.assertEqual(evalRPN(["8", "4", "/"]), 2)

    def test_negative_result(self):
        self.assertEqual(evalRPN(["5", "3", "-"]), 2)

    def test_multiplication(self):
        self.assertEqual(evalRPN(["-2", "3", "*"]), -6)

if __name__ == '__main__':
    unittest.main()

