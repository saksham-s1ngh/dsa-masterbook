from LinkedList import LinkedList
from PrintList import print_list_with_forward_arrow

def find_mid(head):
    
    # Replace this placeholder return statement with your code
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow 

def main():

    input = (
    [7, 10, 14, 21, 22],
    [3, 6, 9, 12],
    [23, 19, 15, 22, 34, 76, 12],
    [5],
    [1, 3, 5, 7, 9, 11,6],
    )

    for i in range(len(input)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(i+1, ".\tInput linked list: ", sep="", end="")
        print_list_with_forward_arrow(input_linked_list.head)
        print("\n\tMiddle Node: ", end="")
        print(find_mid(input_linked_list.head).data)
        print("-"*100)

if __name__ == "__main__":
    main()
