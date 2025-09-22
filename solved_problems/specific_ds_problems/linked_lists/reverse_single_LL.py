from LinkedList import LinkedList
from LinkedListNode import LinkedListNode
from PrintList import print_list_with_forward_arrow

# class LinkedListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

def reverse(head):

    # Replace this placeholder return statement with your code
    prev = None
    temp = current = head

    while current:
        temp = current
        current = current.next
        temp.next = prev
        prev = temp

    return prev

def main():

    inputs = [
        [10, 20, 30, 40, 50],
        [-1, -2, -3, -4, -5, -6],
        [3, 2, 1],
        [12],
        [1, 2],
    ]

    for i in range(len(inputs)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(inputs[i])
        print(i+1, ".\tInput linked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tReversed linked list: ", end="")
        print_list_with_forward_arrow(reverse(input_linked_list.head))
        print("\n", "-"*100)


if __name__ == "__main__":
    main()