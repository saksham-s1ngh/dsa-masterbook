from listNode import ListNode

class LinkedList2():
    def __init__(self):
        self.head = None
        self.length = 0


    def insert_at(self, index, node_value):
        if index == 0:
            if self.head:
                node = ListNode(node_value)
                node.next = self.head
                self.head = node
            else: 
                node = ListNode(node_value)
                self.head = node
            self.length +=1

        elif index <= self.length:
            if self.head:
                node = ListNode(node_value)
                current = self.head
                for _ in range(index - 1):
                    current = current.next
                node.next = current.next
                current.next = node
            else: 
                node = ListNode(node_value)
                self.head = node  
            self.length +=1

        else:
            # raise IndexError("Insertion index out of bounds.")
            print("Insertion index out of bounds.")
        
    def remove_at(self, index):
        if index == 0:
            if self.head:
                node_val = self.head.val
                self.head = self.head.next
                self.length -= 1
                return node_val
            else:
                # raise ValueError("Cannot remove items from empty list.")
                print("Cannot remove items from empty list.")

        elif index < self.length:
            if self.head:
                current = self.head
                for i in range(index - 1):
                    current = current.next
                node_val = current.next.val
                current.next = current.next.next
                self.length -= 1
                return node_val
            else:
                # raise ValueError("Cannot remove items from empty list.")
                print("Cannot remove items from empty list.")
        
        else:
            # raise IndexError("Removal index out of bounds.")
            print("Removal index out of bounds.")

    def peak_at(self, index):
        if index == 0:
            if self.head :
                return self.head
            else:
                return None
        elif index < self.length:
            if self.head:
                current = self.head
                for _ in range(index):
                    current = current.next
                return current
            else:
                return None
        else:
            # raise IndexError("Index out of bounds.")
            print("Index out of bounds.")

    def __str__(self):
        curr = self.head
        if self.head == None:
            return "List is empty"

        result = "Head -> "
        while curr:
            result += f"{curr.val} -> "
            curr = curr.next
        result += "None"

        return result
        
new_list = LinkedList2()
new_list.peak_at(0)
new_list.peak_at(5)
new_list.insert_at(5, 3)
new_list.insert_at(0, 12) # 12 -> 
new_list.insert_at(0, 2) # 2 -> 12 -> 
new_list.insert_at(5, 7)
print(f"Peaking node at index 0: {new_list.peak_at(0)}") # should return 2
print(f"Peaking node at index 1: {new_list.peak_at(1)}")
new_list.insert_at(3, 6)
new_list.insert_at(2, 6) # 2 -> 12 -> 6 ->
print(new_list)
print(f"Removed node at index 0: {new_list.remove_at(0)}") # 12 -> 6 -> 
print(new_list)
print(f"Removed node at index 1: {new_list.remove_at(1)}") # 12 -> 
print(new_list)
new_list.remove_at(2)
new_list.remove_at(1)
print(f"Removed node at index 0: {new_list.remove_at(0)}") # empty list
new_list.remove_at(0)
print(new_list)

