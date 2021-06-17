from singly_linked_list import LinkedList

def remove_duplicates(llist):
    arr = []
    curr = llist.head
    prev = None
    while curr:
        if curr.data not in arr:
            arr.append(curr.data)
            prev = curr
        else:
            prev.next = curr.next
            curr = None

        curr = prev.next

    # cur = llist.head
    # prev = None

    # dup_values = dict()

    # while cur:
    #     if cur.data in dup_values:
    #         # Remove node:
    #         prev.next = cur.next
    #         cur = None
    #     else:
    #         # Have not encountered element before.
    #         dup_values[cur.data] = 1
    #         prev = cur
    #     cur = prev.next
    


    return llist

llist = LinkedList()
llist.append(1)
llist.append(6)
llist.append(1)
llist.append(4)
llist.append(2)
llist.append(2)
llist.append(4)

print("Original Linked List")
llist.print_list()
print("Linked List After Removing Duplicates")
new_list = remove_duplicates(llist)
new_list.print_list()