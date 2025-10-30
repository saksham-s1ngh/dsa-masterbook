"""
Problem link: https://www.educative.io/courses/data-structures-coding-interviews-python/challenge-evaluate-postfix-expression-using-a-stack
"""

from Stack import MyStack


def apply_operator(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 // num2  # Assuming integer division for simplicity

def evaluate_post_fix(exp):
    stack = MyStack()

    for char in exp:
        if char.isdigit():
            # Push numbers in stack
            stack.push(int(char)) # cast the digit char to string before pushing
        else:
            # Operator encountered
            # Pop top two numbers from stack
            right = stack.pop()
            left = stack.pop()
            # Apply operator to operands and push result back to stack
            result = apply_operator(char, left, right)
            stack.push(result)
    # Final result is at the top of the stack
    return stack.pop()

# def postfix_solve(expression):
#     stack = MyStack()
#     exp_len = len(expression)-1
#     while exp_len > 0:
#         stack.push(expression[exp_len])
#         exp_len -= 1

#     s2 = MyStack()

#     while stack.peek():
#         if stack.peek().isdigit():
#             s2.push(stack.pop())
#         else:
#             operator = stack.pop()
#             operand1 = s2.pop()
#             operand2 = s2.pop()
#             stack.push(operate(operand1, operand2, operator))
    
#     return stack.peek()


# def operate(operand1, operand2, operator):
#     if operator == "+":
#         return operand1 + operand2
#     elif operator == "-":
#         return operand1 - operand2
#     elif operator == "*":
#         return operand1 * operand2
#     elif operator == "/":
#         return operand1 / operand2 if operand2 != 0 else operand1