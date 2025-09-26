"""
Problem link: https://www.educative.io/courses/data-structures-coding-interviews-python/challenge-implement-two-stacks-using-one-list

Challenge: Implement Two Stacks Using One List
Try to solve the Implement Two Stacks Using One List problem.

Statement
Design a data structure TwoStacks, that represents two stacks using a single list, where both stacks share the same list for storing elements.

The following operations must be supported:

push1(value): Takes an integer value and inserts it into the first stack.

push2(value): Takes an integer value and inserts it into the second stack.

pop1(): Removes the top element from the first stack and returns it.

pop2(): Removes the top element from the second stack and returns it.

Note: Perform all operations in-place without resizing the underlying list, maintaining a fixed size throughout.
"""
class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.tS = [None]*size
        self.s1_ptr = 0
        self.s2_ptr = len(self.tS) - 1

    # OVERFLOW CONDITION: if stack pointers cross each other.

    # Insert Value in First Stack
    def push1(self, value):
        if not self.s1_ptr > self.s2_ptr:
            self.tS[self.s1_ptr] = value
            self.s1_ptr += 1
            return

        return "Stack over-flow" 

    # Insert Value in Second Stack
    def push2(self, value):
        if not self.s2_ptr < self.s1_ptr:
            self.tS[self.s2_ptr] = value
            self.s2_ptr -= 1
            return

        return "Stack over-flow"

    # UNDERFLOW CONDITION: if stack1 pointer is 0 or if stack2 pointer is
    #   greater than length-1 (last index).   

    # Return and remove top Value from First Stack
    def pop1(self):
        if self.s1_ptr - 1 < 0:
            return "Stack under-flow"
        popped = self.tS[self.s1_ptr - 1]
        self.tS[self.s1_ptr - 1] = None # the element at popped index is reset to 0
        self.s1_ptr -= 1
        return popped

    # Return and remove top Value from Second Stack
    def pop2(self):
        if self.s2_ptr + 1 > len(self.tS) - 1:
            return "Stack under-flow"
        popped = self.tS[self.s2_ptr + 1]
        self.tS[self.s2_ptr + 1] = None # the element at popped index is reset to 0
        self.s2_ptr += 1
        return popped

def main():
    calls = [
        ["TwoStacks", "push1", "push2", "pop2"],
        ["TwoStacks", "push1", "pop1", "push2", "pop2"],  
        ["TwoStacks", "push1", "push2", "push1", "push2", "pop1", "pop2", "pop1"],      
        ["TwoStacks", "push2", "pop2", "push2", "push1"],
        ["TwoStacks", "push1", "push1", "push2", "pop1"],
    ]

    inputs = [
        [5, 10, 15, None],
        [7, -4, None, -6, None],
        [5, 10, 20, 50, 30, None, None, None],
        [10, 4, None, 8, 10],
        [3, 10, 20, 30, None],
    ]

    for i in range(len(calls)):
        print(f"Testcase {i + 1}:")
        stack_obj = TwoStacks(inputs[i][0])

        for j in range(1, len(calls[i])):
            if calls[i][j] == "push1":
                stack_obj.push1(inputs[i][j])
            elif calls[i][j] == "push2":
                stack_obj.push2(inputs[i][j])
            elif calls[i][j] == "pop1":
                print(f"\tpop1 returns {stack_obj.pop1()}")
            elif calls[i][j] == "pop2":
                print(f"\tpop2 returns {stack_obj.pop2()}")

        print("-" * 50)


if __name__ == "__main__":
    main()