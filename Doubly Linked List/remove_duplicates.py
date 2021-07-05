from doubly_linked_list import DoublyLinkedList

def remove_duplicates(dllist):
    cur = dllist.head
    dup = []
    while cur:
        if cur.data not in dup:
            dup.append(cur.data)
            cur = cur.next
        else:
            nxt = cur.next
            dllist.delete_node(cur)
            cur = nxt
        

dllist = DoublyLinkedList()
dllist.append(8)
dllist.append(4)
dllist.append(4)
dllist.append(6)
dllist.append(4)
dllist.append(8)
dllist.append(4)
dllist.append(10)
dllist.append(12)
dllist.append(12)


remove_duplicates(dllist)
dllist.print_list()