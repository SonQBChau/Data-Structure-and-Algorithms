class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self, data):
        pass

    def append(self, data):
        # if empty, we create a head node first
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else: 
            new_data = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_data
            new_data.next = self.head

    def print_list(self):
        pass