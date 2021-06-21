from singly_linked_list import LinkedList

def count_occurences_iterative(llist, data):
    cur = llist.head
    count = 0
    while cur:
        if cur.data == data:
            count += 1
        cur = cur.next
    return count
    
def count_occurences_recursive(llist, node, data):
    if not node:
        return 0
    if node.data == data:
        return 1 + count_occurences_recursive(llist, node.next, data)
    else:
        return count_occurences_recursive(llist, node.next, data)


llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

llist_2 = LinkedList()
llist_2.append(1)
llist_2.append(2)
llist_2.append(1)
llist_2.append(3)
llist_2.append(1)
llist_2.append(4)
llist_2.append(1)
print(count_occurences_iterative(llist_2,1))
print(count_occurences_recursive(llist_2,llist_2.head, 1))