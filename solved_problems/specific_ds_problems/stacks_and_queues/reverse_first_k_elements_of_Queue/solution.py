from Queue import MyQueue
from Stack import MyStack

# MY FIRST ATTEMPT: NOT AT IN-PLACE MODIFYING ALGORITHM
#   INSTEAD RETURNS A NEW QUEUE
def reverse_k_elements_myFA(queue, k):
    
    # Replace this placeholder return statement with your code
    input_q_size = queue.size()
    if k < 1 or k > input_q_size: 
        return None
        
    
    k_reversed_q = MyQueue()
    rev_stack = MyStack()
    
    # i = 0
    # while i < k:
    for _ in range(k):
        rev_stack.push(queue.dequeue())
        # i += 1
        
    while rev_stack.size():
        k_reversed_q.enqueue(rev_stack.pop()) 
    
    # while i < input_q_size:
    while queue.size():
        k_reversed_q.enqueue(queue.dequeue())
        # i += 1
    
    return k_reversed_q

# 1. Push the first k elements in the queue in a stack
# 2. Pop the stack elements and enqueue them at the end of queue
# 3. Dequeue queue elements till k and append them at the end of the queue

def revers_k_elements(queue, k):
    # Handling invalid input
    if queue.is_empty() is True or k > queue.size() or k < 0:
        return None

    stack = MyStack()
    for i in range(k):
        stack.push(queue.dequeue())

    while stack.is_empty() is False:
        queue.enqueue(stack.pop())
        
    size = queue.size()
    for i in range(size - k):
        queue.enqueue(queue.dequeue())

    return queue


if __name__ == "__main__":
    test_cases = [
        [1,2,3,4,5,6,7,8,9,10],
        [-2,1,-5,45,6,3,-9],
        [1,2,5,0,7,4,23],
        [7,3,5,6,8,12],
        [5,67,43,23,12,56,78,98,6,21,9]
    ]
    k_values = [4, 10, -7, 5, 2]
    for i in range(len(test_cases)):
        queue = MyQueue()
        for item in test_cases[i]:
            queue.enqueue(item)
        k = k_values[i]
        print(i+1, "\tOriginal Queue:", queue.queue_list)
        print("\tk value:", k)
        reversed_queue = revers_k_elements(queue, k)
        print("\tQueue after reversal:" , queue.queue_list)
        print("-"*100)