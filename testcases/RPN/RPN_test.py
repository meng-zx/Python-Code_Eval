import unittest
from RPN import evalRPN  # Import the function from your script

class TestEvalRPN(unittest.TestCase):

    def test_division(self):
        self.assertEqual(evalRPN(["8", "4", "/"]), 2)

    def test_negative_result(self):
        self.assertEqual(evalRPN(["5", "3", "-"]), 2)

    def test_multiplication(self):
        self.assertEqual(evalRPN(["-2", "3", "*"]), -6)

    def test_example_1(self):
        tokens = ["2", "1", "+", "3", "*"]
        self.assertEqual(evalRPN(tokens), 9)

    def test_example_2(self):
        tokens = ["4", "13", "5", "/", "+"]
        self.assertEqual(evalRPN(tokens), 6)

    def test_example_3(self):
        tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        self.assertEqual(evalRPN(tokens), 22)

    def test_empty_tokens(self):
        tokens = []
        with self.assertRaises(IndexError):
            evalRPN(tokens)

    def test_single_operand(self):
        tokens = ["42"]
        self.assertEqual(evalRPN(tokens), 42)

    def test_single_operator(self):
        tokens = ["+"]
        with self.assertRaises(IndexError):
            evalRPN(tokens)

    def test_invalid_token(self):
        tokens = ["2", "1", "+", "3", "x"]
        with self.assertRaises(ValueError):
            evalRPN(tokens)

    def test_large_numbers(self):
        tokens = ["200", "200", "+"]
        self.assertEqual(evalRPN(tokens), 400)

    def test_negative_numbers(self):
        tokens = ["-10", "5", "+", "-3", "*"]
        self.assertEqual(evalRPN(tokens), -15)

    def test_division_by_zero(self):
        tokens = ["5", "0", "/"]
        with self.assertRaises(ZeroDivisionError):
            evalRPN(tokens)

    def test_mixed_operators(self):
        tokens = ["4", "5", "+", "7", "3", "-", "*"]
        self.assertEqual(evalRPN(tokens), 27)

    def test_large_expression(self):
        tokens = ["2"] * 1000 + ["*"]
        self.assertEqual(evalRPN(tokens), 2 ** 1000)

    def test_strange_case_1(self):
        tokens = ["0", "3", "5", "4", "+", "*", "-"]
        self.assertEqual(evalRPN(tokens), -32)

    def test_strange_case_2(self):
        tokens = ["1", "-1", "+", "1", "-1", "+", "+"]
        self.assertEqual(evalRPN(tokens), 0)

if __name__ == '__main__':
    unittest.main()

