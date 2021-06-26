from singly_linked_list import LinkedList

def move_tail_to_head(llist):
    cur = llist.head
    head = llist.head
    prev = None
    while cur.next:
        prev = cur
        cur = cur.next
    # move tail to head
    # point tail next to old head
    # point prev tail to None
    prev.next = None
    cur.next = head
    llist.head = cur

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
move_tail_to_head(llist)
llist.print_list()