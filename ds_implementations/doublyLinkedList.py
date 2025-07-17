class ListNode2():
    def __init__(self, value=False):
        self.val = value
        self.next = self.prev = None

    def __str__(self):
        return str(self.val)
    
    def __repr__(self):
        return f"ListNode: (val = {repr(self.val)}, next = {repr(self.next)})"


class DoublyLinkedList():
    def __init__(self):
        self.head = self.tail = None
        self.length = 0

    def _is_valid_index(self, index, allow_end=False):
        # will usually be True only for insertion, since elements can be inserted at the end of list, 
        #   position == length (technically, an invalid index since last valid index == length - 1)
        if allow_end: 
            return 0 <= index <= self.length
        
        #but for removal, we can't remove from the index == length, since no element exists at that index
        return 0 <= index < self.length 

    def _get_node_at(self, index):
        if not self._is_valid_index(index):
            return None
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def insert_at(self, index, value):
        if not self._is_valid_index(index, allow_end=True):
            # raise IndexError("Insertion index out of bounds!")
            print("Out of bounds")
            return

        new_node = ListNode2(value)

        if self.length == 0: # empty list insertion
            self.head = self.tail = new_node
            self.length += 1
            return

        if index == 0: # insertion at head
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        elif 0 < index < self.length :
            current = self._get_node_at(index)
            current.prev.next = new_node
            new_node.prev = current.prev
            current.prev = new_node
            new_node.next = current
        else: # insertion at tail
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
        self.length += 1

    def remove_at(self, index):
        if self.head is None:
            # raise ValueError("Empty list")
            print("Empty list")
            return

        if not self._is_valid_index(index):
            # raise IndexError("Removal index out of bounds!")
            print("Out of bounds")
            return
        
        current = self._get_node_at(index)

        if self.length == 1:
            self.head = self.tail = None

        if index == 0: # removal at head
            self.head = current.next
            current.next.prev = None
        elif 0 < index < self.length - 1:
            current.prev.next = current.next
            current.next = current.prev

        self.length -= 1
        return current.val

    def peak_at(self, index):
        if not self._is_valid_index(index):
            # raise IndexError("Invalid index")
            print("Index out of bounds")
            return
        
        return self._get_node_at(index).val
    

myDList = DoublyLinkedList()
myDList.insert_at(1,3) # won't work
myDList.insert_at(0,3) # 3 <-> None
myDList.peak_at(1)
myDList.peak_at(0)
myDList.insert_at(1, 5) # 3 <-> 5 <-> None
