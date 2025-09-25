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
    result = None
    current1 = head1

    # Iterate over each node in the first list
    while current1:
        current2 = head2
        # Compare each node in the first list with each node in the second list
        while current2:
            # If a common element is found and it's not already in the result list, add it
            if current1.data == current2.data and not exists_in_result(current1.data, result):
                result = insert_at_head(result, current1.data)
            current2 = current2.next
        current1 = current1.next

    return result

# Function to check if a data value exists in the result list
def exists_in_result(data, head):
    current = head
    while current:
        if current.data == data:
            return True
        current = current.next
    return False

def insert_at_head(head, data):
    new_node = LinkedListNode(data)
    new_node.next = head
    return new_node


def main():
    union_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 1, 2, 2, 3, 3, 4, 4, 5],
        [-45, 34, -54, 45, -65, 54],
        [12],
        [0, 1, 2],
    ]

    intersection_list = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 1, 2, 2, 3, 3, 4, 4, 5],
        [-45, 34, -54, 45, -65, 54],
        [12],
        [0, 1, 2],
    ]

    input_list2 = [
        [7, 8, 9, 10, 11, 12, 13, 14],
        [1, 2, 3, 4, 5, 6],
        [3, 2, 1],
        [12],
        [3, 4, 5],
    ]

    for i in range(len(union_list)):
        input_linked_list1 = LinkedList()
        input_linked_list2 = LinkedList()
        input_linked_list3 = LinkedList()

        input_linked_list1.create_linked_list(union_list[i])
        input_linked_list2.create_linked_list(intersection_list[i])
        input_linked_list3.create_linked_list(input_list2[i])
        
        print(i+1, ".\tInput linked list 1: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list1.head)
        
        print("\n\tInput linked list 2: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list3.head)
        
        print("\n\n\tUnion: ", end="")
        print_list_with_forward_arrow(union(input_linked_list1.head, input_linked_list3.head))

        print("\n\tIntersection: ", end="")
        print_list_with_forward_arrow(intersection(input_linked_list2.head, input_linked_list3.head))
        print("\n", "-"*100)


if __name__ == "__main__":
    main()