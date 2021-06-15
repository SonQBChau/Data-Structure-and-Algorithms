class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def print_list(self) -> None:
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
    
    def prepend(self, data) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")

llist.prepend("D")

llist.print_list()  