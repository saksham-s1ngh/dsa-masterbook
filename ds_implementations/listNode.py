class ListNode():
    # defines the node having a val attribute that can take any value of type T (Generic)
    #   and the next pointer can either point to another ListNode or nothing(None)
    def __init__(self, val = None, next = None): 
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return f"ListNode: (val = {repr(self.val)}, next = {repr(self.next)})" # avoid for circular LL