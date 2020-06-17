# singly-linked

class  Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return f"<HashTableEntry('{self.value}', '{self.next}')>"
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
    
    def delete(self, value):
        cur = self.head
        # Special case - deleting the head
        if cur.value == value:
            self.head = self.head.next
            return cur
        
        # General case
        prev = cur
        cur = cur.next
        while cur is not None:
            if cur.value == value: # Delete this one
                prev.next = cur.next # Cuts out the old node
                return cur
            else:
                prev = prev.next
                cur = cur.next
                
        return None
        
        
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_head(Node(11))