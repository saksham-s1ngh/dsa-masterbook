from LinkedList import LinkedList
from LinkedListNode import LinkedListNode
from PrintList import print_list_with_forward_arrow

# Definition for a linked list node
# class LinkedListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
def remove_duplicates(head):
    
    # Replace this placeholder return statement with your code
    originals = {}
    # temp = curr = head
    # prev = temp
    # while curr:
    #     if curr.data in originals:
    #         temp = curr
    #         prev.next = temp.next
    #         temp = None
    #     originals[curr.data]= originals.get(curr.data, 0) + 1
    #     prev = curr
    #     curr = curr.next
    
    curr = head
    prev = None
    while curr:
        if curr.data in originals:
            prev.next = curr.next
            
        originals[curr.data] = originals.get(curr.data, 0) + 1
        prev = curr
        curr = curr.next
        
    return head

def main():

    inputs = [
        [30, 20, 30, 10, 50],
        [-7, -7, -22, -1, -5, -5],
        [1, 1, 1],
        [9, -9, 9],
        [1, -2, -2],
    ]

    for i in range(len(inputs)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(inputs[i])
        print(i + 1, ".\tInput linked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tLinked list without duplicates: ", sep="", end="")
        print_list_with_forward_arrow(remove_duplicates(input_linked_list.head))

        print("\n", "-" * 100)


if __name__ == "__main__":
    main()