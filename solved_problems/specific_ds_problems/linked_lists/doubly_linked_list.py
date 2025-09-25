from doubly_linked_list_node import DoublyLinkedListNode

# Template for the doubly linked list
class DoublyLinkedList:
    # __init__ will be used to make a DoublyLinkedList type object.
    def __init__(self):
        self.head = None

    # insert_node_at_head method will insert a DoublyLinkedListNode at the head
    # of a linked list.
    def insert_node_at_head(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = node

    # create_linked_list method will create the linked list using the
    # given integer array with the help of insert_node_at_head method.
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = DoublyLinkedListNode(x)
            self.insert_node_at_head(new_node)
    
    # __str__(self) method will display the elements of linked list.
    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        return result