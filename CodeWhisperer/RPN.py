def evalRPN(tokens):
    stack = []

    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: int(x / y)
    }

    for token in tokens:
        if token in ops:
            op = ops[token]
            y = stack.pop()
            x = stack.pop()
            result = op(x, y)
            stack.append(result)
        else:
            stack.append(int(token))

    return stack.pop()
