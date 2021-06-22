from singly_linked_list import LinkedList
def rotate(llist, k):
    if llist.head and llist.head.next:
        p = llist.head 
        q = llist.head 
        prev = None
        count = 0
        # move p to the pivot k
        while p and count < k:
            prev = p
            p = p.next 
            q = q.next 
            count += 1
        
        # move q to the end
        prev  = None
        while q:
            prev = q 
            q = q.next 
        q = prev 

        # make circular linked list
        q.next = llist.head

        # point the head to the new node
        llist.head = p.next
        p.next = None
    

    return llist

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)

llist_2 = rotate(llist, 4)
llist_2.print_list()