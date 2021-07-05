from doubly_linked_list import DoublyLinkedList

def pairs_with_sum(dllist, sum_val):  
    pairs = list()
    p = dllist.head
    q = None
    while p:
        q = p.next
        while q:
            if (q.data + p.data) == sum_val:
                pairs.append("(" + str(p.data) + "," + str(q.data) + ")")
            q = q.next
        p = p.next
    return pairs

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)

print(pairs_with_sum(dllist, 5))