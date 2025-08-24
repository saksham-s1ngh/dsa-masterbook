from node import Node

class LinkedList: 
    def __init__(self):
        self.head = None
        self.length = 0

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node doesn't exist.")
            return 
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def insert_at_end(self, node: Node):
        # if no head exists and length is also 0 (obv, if no head)
        if not self.head and self.length == 0: 
            self.head = node
            self.length += 1
            return
        
        # if list is populated, traverse till last node
        current = self.head
        while current and current.next :
            current = current.next

        # increment list length
        self.length += 1

        # point last node to new node 
        if current:
            current.next = node
        node.next = None # don't think we need this condition, except for safety (by default, node.next = None)
        
        # free up memory, since python has auto garbage collection no need for explicit command 
        # current = None

    def delete_node(self, key):
        cur_node = self.head

        # if key is in head
        if cur_node and cur_node.val == key:
            self.head = cur_node.next
            cur_node = None
            return 

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None: # key not in list
            return 

        prev.next = cur_node.next
        cur_node = None

    def remove_from_end(self):
        if self.length == 0:
            return None

        if self.length == 1: # only node in the list is the head
            node = self.head
            self.head = None
            self.length -= 1
            return node
        
        # if list is populated, iterate till 2ND LAST NODE
        #   since we want to remove the last, so we need to stop at 2nd last node
        #   to re-allocate pointers and remove the last node
        current = self.head
        
        # to resolve pylance warnings and to tell compiler to trust: current != None
        assert current is not None 

        # below won't work with a single node in the list
        #   single node case handled above
        while current and current.next and current.next.next :
            current = current.next
        
        self.length -= 1

        # to resolve pylance warnings and to tell compiler to trust: current.next != None
        assert current.next is not None

        end_node_value = current.next.val # since current would be pointing to 2nd last element, current.next -> last element
        current.next = None # delete the last node after saving its value

        return end_node_value

    def peek_end(self):
        current = self.head

        while current and current.next:
            current = current.next
        
        return current.val if current else None
    
    def __str__(self):
        curr = self.head
        if self.head == None:
            print("List is empty")
            return ""

        result = "Head -> "
        while curr:
            result += f"{curr.val} -> "
            curr = curr.next
        result += "None"

        return result

my_list = LinkedList()
print(my_list)
print(my_list.remove_from_end())
my_list.insert_at_end(Node(7))
print(my_list)
my_list.peek_end()
print(my_list.remove_from_end())
my_list.insert_at_end(Node(8))
print(my_list)
my_list.insert_at_end(Node(2))
print(my_list)
my_list.insert_at_end(Node(9))
print(my_list)