from LinkedList import LinkedList
from LinkedListNode import LinkedListNode
from PrintList import print_list_with_forward_arrow, print_list_with_forward_arrow_cycle


def detect_cycle_myfa(head):
    
    # Replace this placeholder return statement with your code
    fast = slow = head
    while slow and fast:
        if slow == fast:
            return True
            
        slow = slow.next
        fast = fast.next.next
    return False

def detect_cycle(head):

    fast = slow = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # the if condition should come after otherwise
        #   the loop breaks on the first iteration
        #   since both fast and slow point to the same
        #   node on the first iteration.
        if slow == head:
            return True
        
    return False
    
# Driver code
def main():

    input = (
             [2, 4, 6, 8, 10, 12],
             [1, 3, 5, 7, 9, 11],
             [0, 1, 2, 3, 4, 6],
             [3, 4, 7, 9, 11, 17],
             [5, 1, 4, 9, 2, 3],
            )
    pos = [0, -1, 1, -1, 2]
    j = 1

    for i in range(len(input)):

        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(input[i])
        print(f"{j}.\tInput: ", sep="", end="")
        if pos[i] == -1:
            print_list_with_forward_arrow(input_linked_list.head)
        else:
            print_list_with_forward_arrow_cycle(input_linked_list.head)
        print("\n\tPosition:", pos[i])
        if pos[i] != -1:
            length = input_linked_list.get_length(input_linked_list.head)
            last_node = input_linked_list.get_node(input_linked_list.head, length - 1)
            last_node.next = input_linked_list.get_node(input_linked_list.head, pos[i])

        print(f"\n\tDetected cycle = {detect_cycle(input_linked_list.head)}")
        j += 1
        print("-"*100, "\n")


if __name__ == "__main__":
    main()
