import LinkedListNode

# Definition for a linked list node
# class LinkedListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

def search(head, value):

    # Replace this placeholder return statement with your code
    if head is None:
        return False
    
    curr_node = head
    while curr_node:
        if curr_node.data == value:
            return True
        curr_node = curr_node.next
    
    return False