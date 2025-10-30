"""
Problem link: https://www.educative.io/courses/data-structures-coding-interviews-python/challenge-evaluate-postfix-expression-using-a-stack
"""

from Stack import MyStack

def postfix_solve(expression):
    stack = MyStack()
    exp_len = len(expression)-1
    while exp_len > 0:
        stack.push(expression[exp_len])
        exp_len -= 1

    s2 = MyStack()

    while stack.peek():
        if stack.peek().isdigit():
            s2.push(stack.pop())
        else:
            operator = stack.pop()
            operand1 = s2.pop()
            operand2 = s2.pop()
            stack.push(operate(operand1, operand2, operator))
    
    return stack.peek()


def operate(operand1, operand2, operator):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2 if operand2 != 0 else operand1