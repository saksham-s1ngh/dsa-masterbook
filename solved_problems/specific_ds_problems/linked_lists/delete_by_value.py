from LinkedList import LinkedList
from LinkedListNode import LinkedListNode
from PrintList import print_list_with_forward_arrow

# Definition for a linked list node
# class LinkedListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

def delete_my(head, value):
    
    # Replace this placeholder return statement with your code
    # NOTE: THIS CODE ACTUALLY DOESN'T AFFECT THE LIST SINCE IN AN ACTUAL DELETION METHOD FOR A LINKEDLIST
    #   WE'D EITHER NEED TO ADJUST THE SELF.HEAD EXPLICITLY TO CHANGE THE HEAD, OR SEND THE HEAD VARIABLE
    #   INTO THE METHOD AND THEN RETURN THE CORRECTED HEAD FROM THIS METHOD.

    if not head:
        return False

    curr_node = head
    if curr_node.data == value:
        curr_node = curr_node.next
        head = curr_node
        return True

    while curr_node.next:
        if curr_node.next.data == value:
            curr_node.next = curr_node.next.next
            return True

        curr_node = curr_node.next

    return False

def delete(head, value):
    deleted = False

    current = head
    previous = None

    # check if the head contains the value to be deleted
    if current.data == value:
        head = head.next
        deleted = True
        return deleted
    
    # traverse to find the node with the given value
    while current is not None:
        if value == current.data:
            previous.next = current.next
            current.next = None
            deleted = True
            break

        previous = current
        current = current.next

    return deleted


def main():

    inputs = [
        [10, 20, 30, 40, 50],
        [-1, -2, -3, -4, -5, -6],
        [3, 2, 1],
        [12],
        [1, 2],
    ]

    values = [30, -8, 3, 12, 1]

    for i in range(len(inputs)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(inputs[i])
        print(i+1, ".\tInput linked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tValue to be deleted: ", values[i], sep="", end="")
        print("\n\n\tResult: ", delete(input_linked_list.head, values[i]), end=" ,")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n", "-"*100)


if __name__ == "__main__":
    main()