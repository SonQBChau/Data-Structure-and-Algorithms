from singly_linked_list import LinkedList

def merge_sorted(llist_1, llist_2) -> LinkedList:
    p = llist_1.head
    q = llist_2.head
    s = None

    if not p:
        return q
    if not q: 
        return p
    
    if p and q:
        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next
        new_head = s

    while p and q:
        if p.data <= q.data:
            s.next = p
            s = p
            p = s.next
        else:
            s.next = q
            s = q
            q = s.next
    if not p:
        s.next = q
    if not q:
        s.next = p
    
    llist_1.head = new_head
    return llist_1

llist_1 = LinkedList()
llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

sorted_list = merge_sorted(llist_1, llist_2)
sorted_list.print_list()