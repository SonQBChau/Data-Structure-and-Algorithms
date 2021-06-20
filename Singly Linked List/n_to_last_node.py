from singly_linked_list import LinkedList
def print_nth_from_last(llist, n, method):
    if method == 1:
        #Method 1:
        total_len = llist.len_iterative()

        cur = llist.head
        while cur:
            if total_len == n:
                return cur.data
            total_len -= 1
            cur = cur.next

        if cur is None:
            return 
    elif method == 2:
        # Method 2:
        p = llist.head
        q = llist.head

        # move q to n position
        if n > 0:
            count = 0
            while q:
                count += 1
                if count >= n:
                    break
                q = q.next
        
            if not q: 
                print(str(n) + " is greater than the number of nodes in list.")
                return
            
            # now we find the position til the end
            # increase both p and q until the end of q
            while q.next:
                p = p.next
                q = q.next
            return p.data
        else:
            return None



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print(print_nth_from_last(llist, 4,1))
print(print_nth_from_last(llist, 4,2))