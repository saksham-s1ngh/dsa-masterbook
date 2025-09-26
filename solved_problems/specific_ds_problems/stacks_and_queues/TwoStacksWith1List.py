class TwoStacks:
    # Initialize the two stacks here
    def __init__(self, size):
        self.tS = [0]*size
        self.s1_ptr = 0
        self.s2_ptr = len(self.tS) - 1

    # Insert Value in First Stack
    def push1(self, value):
        if self.tS[self.s1_ptr] == 0 and not self.s1_ptr > self.s2_ptr:
            self.tS[self.s1_ptr] = value
            self.s1_ptr += 1
            return

        return "Stack over-flow" 

    # Insert Value in Second Stack
    def push2(self, value):
        if self.tS[self.s2_ptr] == 0 and not self.s2_ptr < self.s1_ptr:
            self.tS[self.s2_ptr] = value
            self.s2_ptr -= 1
            return

        return "Stack over-flow"

    # Return and remove top Value from First Stack
    def pop1(self):
        if self.s1_ptr - 1 < 0:
            return "Stack under-flow"
        popped = self.tS[self.s1_ptr - 1]
        self.tS[self.s1_ptr] = 0
        self.s1_ptr -= 1
        return popped

    # Return and remove top Value from Second Stack
    def pop2(self):
        if self.s2_ptr + 1 > len(self.tS) - 1:
            return "Stack under-flow"
        popped = self.tS[self.s2_ptr + 1]
        self.tS[self.s2_ptr] = 0
        self.s2_ptr += 1
        return popped