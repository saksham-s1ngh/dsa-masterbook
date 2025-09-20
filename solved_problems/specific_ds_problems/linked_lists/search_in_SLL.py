import LinkedListNode
from LinkedList import LinkedList
from PrintList import print_list_with_forward_arrow

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

def search_recursive(head, value):

    if not head:
        return False
    
    if head.data == value:
        return True
    
    search_recursive(head.next, value)
    

def main():
    inputs = [
        [10, 20, 30, 40, 50],
        [-1, -2, -3, -4, -5, -6],
        [3, 2, 1],
        [],
        [12],
    ]
    value = [50, -7, 3, 55, 12]

    for i in range(len(inputs)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(inputs[i])
        if len(inputs[i]) == 0:
            print(i+1, ".\tInput linked list: null", sep="", end="")
        else:
            print(i+1, ".\tInput linked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tSearched value: ", value[i] )
        print("\n\tSingly linked list value found : ", search_recursive(input_linked_list.head, value[i]) )
        print("\n", "-"*100)


if __name__ == "__main__":
    main()