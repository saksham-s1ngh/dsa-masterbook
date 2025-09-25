from doubly_linked_list import DoublyLinkedList
from doubly_linked_list_node import DoublyLinkedListNode
from PrintList import print_list_with_arrows

def is_palindrome(head):
    
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