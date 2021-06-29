from singly_linked_list import LinkedList
def sum_two_lists(llist_1, llist_2):
    llist_3 = LinkedList()
    p = llist_1.head
    q = llist_2.head

    carry = 0
    while p or q:
        if not p:
            i = 0
        else:
            i = p.data
        if not q:
            j = 0
        else:
            j = q.data
        s = i + j + carry
        if s >= 10:
            r = s % 10
            carry = 1
            llist_3.append(r)
        else:
            carry = 0
            llist_3.append(s)
        if p:
            p = p.next
        if q:
            q = q.next
     
    return llist_3

llist_1 = LinkedList()
llist_1.append(5)
llist_1.append(6)
llist_1.append(3)

llist_2 = LinkedList()
llist_2.append(8)
llist_2.append(4)
llist_2.append(2)

llist_3 = LinkedList()
llist_3 = sum_two_lists(llist_1, llist_2)
llist_3.print_list()