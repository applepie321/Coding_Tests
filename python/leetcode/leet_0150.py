# Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=daily-question&envId=2024-01-30

def eval_RPN(tokens):
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if token == '+':
                stack.append(num1 + num2)
            elif token == '-':
                stack.append(num1 - num2)
            elif token == '*':
                stack.append(num1 * num2)
            elif token == '/':
                stack.append(int(num1 / num2))

    return stack.pop()
