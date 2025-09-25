from doubly_linked_list import DoublyLinkedList
from doubly_linked_list_node import DoublyLinkedListNode
from PrintList import print_list_with_arrows

def is_palindrome_myFA(head):
    
    # Replace this placeholder return statement with your code
    tail = head
    length = 0
    while tail.next:
        tail = tail.next
        length += 1
    
    curr = head
    count = 0
    while count < length // 2 + 1:
        if curr.data != tail.data:
            return False
        curr = curr.next
        tail = tail.prev
        count += 1
    return True
    
def is_palindrome(head):
    start = head  
    end = get_tail_node(head)  

    # If list is empty, it is a palindrome
    if start is None:  
        return True

    # Otherwise, traverse list from both sides
    while start != end and start.prev != end:  

        # If data mismatches at any point, list is not a palindrome
        if start.data != end.data:  
            return False
        start = start.next
        end = end.prev

    #  If data didn't mismatch at any point, list is a palindrome
    return True  

def get_tail_node(head):
    temp = head
    while temp.next is not None:
        temp = temp.next
    return temp

def main():
    input = (
                [2, 4, 6, 4, 2],
                [0, 3, 5, 5, 0],
                [9, 7, 4, 4, 7, 9],
                [5, 4, 7, 9, 4, 5],
                [5, 9, 8, 3, 8, 9, 5],
            )
    j = 1

    for i in range(len(input)):
        input_linked_list = DoublyLinkedList()
        input_linked_list.create_linked_list(input[i])
        head = input_linked_list.head
        print(j, ".\tDoubly Linked List:", end=" ", sep="")
        print_list_with_arrows(head)
        print("\n\n\tIs it a palindrome?", "Yes" if is_palindrome(head) else "No")
        j += 1
        print("-"*100, "\n")

if __name__ == "__main__":
    main()