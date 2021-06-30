from circular_linked_list import CircularLinkedList
from singly_linked_list import LinkedList

def is_circular_linked_list(input_list):
    if input_list.head:
        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False
    else:
        return False

cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print(is_circular_linked_list(cllist))
print(is_circular_linked_list(llist))
