"""
Problem url: https://www.educative.io/courses/data-structures-coding-interviews-python/challenge-implement-queue-using-stacks
"""

from Stack import MyStack
# Push Function => stack.push(int)  //Inserts the element at top
# Pop Function => stack.pop()       //Removes and returns the element at top
# Top/Peek Function => stack.get_top()  //Returns top element
# Helper Functions => stack.is_empty() & stack.isFull() //Returns boolean

class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        # Write your code here
        self.sub_stack = MyStack()
        

    # Inserts the element in the queue
    def enqueue(self, value):
        # Just push all the inserted values into the main stack
        self.main_stack.push(value)
        return

    # Removes the element from the queue
    def dequeue(self):
        # we always pop from the sub_stack since the main_stack will order elements as a stack
        #   and to get the queue ordering we first pop all main stack elements -> push them 
        #   into the sub_stack and then pop.
        # if the sub_stack is empty, we first push all the main_stack elements into the sub_stack
        #   and then pop the element from the sub_stack
        if self.sub_stack.is_empty():
            while self.main_stack.size():
                self.sub_stack.push(self.main_stack.pop())
        
        return self.sub_stack.pop()
    
    def peek(self):
        # return the top element on the sub-stack if not empty
        # if sub_stack is empty then we first push all elements from the main_stack
        #   into the sub_stack.
        if self.sub_stack.is_empty():
            while not self.main_stack.is_empty():
                self.sub_stack.push(self.main_stack.pop())
        
        return self.sub_stack.peek()
    
    def is_empty(self):
        return self.sub_stack.is_empty and self.main_stack.is_empty

def main():
    calls = [["NewQueue","enqueue()","enqueue()","enqueue()","dequeue()"],
             ["NewQueue","enqueue()","dequeue()","enqueue()","dequeue()"],
             ["NewQueue","enqueue()","enqueue()","dequeue()","dequeue()"],
             ["NewQueue","enqueue()","enqueue()","dequeue()","enqueue()"],
             ["NewQueue","enqueue()","dequeue()","enqueue()","enqueue()"]
    
    ]

    inputs = [[None, 3, 4, 5, None],
              [None, -1, None, -4, None],
              [None, 200, 700, None, None],
              [None, -100, -100, None, -100],
              [None, 100000, None, -100000, 4000]
    ]

    for i in range(len(calls)):
        queue_obj = NewQueue()

        print(i + 1, ".\t Starting operations:", sep="")

        # Initialize a queue
        # Loop over all the commands
        for j in range(len(calls[i])):
            if calls[i][j] == "enqueue()":
                inputstr = "enqueue" + \
                    "("+str(inputs[i][j])+")"
                print("\t\t", inputstr, sep="")
                queue_obj.enqueue(inputs[i][j])
            if calls[i][j] == "dequeue()":
                inputstr = "dequeue" + \
                    "("+")"
                print("\t\t", inputstr, "   returns ",
                      queue_obj.dequeue(), sep="")

        print("-" * 100)


if __name__ == "__main__":
    main()