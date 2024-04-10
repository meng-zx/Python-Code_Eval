def evalRPN(tokens):
    # Initialize the result as 0
    result = 0

    # Iterate through the tokens
    for token in tokens:
        # If the token is an integer, add it to the result
        if token.isdigit():
            result += int(token)

        # If the token is an operator, perform the operation
        elif token in {'+', '-', '*', '/'}:
            # Get the operands
            left = evaluate_expression(tokens[:token.index(' ')])
            right = evaluate_expression(tokens[token.index(' ') + 1:])

            # Perform the operation
            if token == '+':
                result += left + right
            elif token == '-':
                result -= left - right
            elif token == '*':
                result *= left * right
            elif token == '/':
                if right != 0:
                    result = result // right
                else:
                    raise ValueError("Invalid division by zero")

    return result
