from LinkedList import LinkedList
from LinkedListNode import LinkedListNode
from PrintList import print_list_with_forward_arrow

# class LinkedListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

def union(head1, head2):

    # Replace this placeholder return statement with your code
    if head1 and head2:
        curr = head1
        while curr.next:
            curr = curr.next
        curr.next = head2
        
        outer = head1
        while outer.next:
            inner = outer.next
            while inner.next:
                if inner.next.data == outer.data:
                    inner.next = inner.next.next
                inner = inner.next
            outer = outer.next
        return head1
        
    return head1 if head2 == None and head1 else head2

def intersection(head1, head2):
    
    # Replace this placeholder return statement with your code
    
    return head1 if head2 == None and head1 else head2