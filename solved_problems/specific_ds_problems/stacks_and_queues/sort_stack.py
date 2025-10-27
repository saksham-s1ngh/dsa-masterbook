"""
Problem link: https://www.educative.io/courses/data-structures-coding-interviews-python/challenge-sort-values-in-a-stack

Brute Implementation (iterative):
1. Use a second temp_stack.
2. Pop value from mainStack.
3. If the value is greater or equal to the top of temp_stack,
  then push the value in temp_stack
  else pop all values from temp_stack
      and push them in mainStack
      and in the end push value in temp_stack
4. Repeat from step 2 till the mainStack is not empty.
5. When mainStack will be empty,
    temp_stack will have sorted values in descending order.
6. Now transfer values from temp_stack to mainStack
    to make values sorted in ascending order.
"""

from Stack import MyStack

def sort_stack(stack):
    if stack.size() < 1:
        return stack

    temp_stack = MyStack()
    while not stack.is_empty():
        value = stack.pop()
        if temp_stack.peek()!= None and value >= temp_stack.peek():
            temp_stack.push(value)
        else:
            while not temp_stack.is_empty() and temp_stack.peek() > value:
                stack.push(temp_stack.pop())
            temp_stack.push(value)
    
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack

def main():
    inputs = [
        [10, 30, 5, 20, 50],
        [-1, -2, -3, -4, -5, -6],
        [3, 2, -1],
        [12],
        [1, -2],
    ]

    for stack_values in inputs:
        stack = MyStack()
        for value in stack_values:
            stack.push(value)
        print("Original Stack:", stack_values)  # Print the original stack values from inputs array
        sorted_stack = sort_stack(stack)
        sorted_items = [sorted_stack.pop() for _ in range(sorted_stack.size())]
        print("Sorted Stack:", sorted_items)  # Print the sorted stack using pop()
        print("-" * 75)


if __name__ == "__main__":
    main()
