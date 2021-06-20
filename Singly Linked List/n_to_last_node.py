from singly_linked_list import LinkedList
def print_nth_from_last(llist, n, method):
    total_len = llist.len_iterative()

    cur = llist.head
    while cur:
        if total_len == n:
            return cur.data
        total_len -= 1
        cur = cur.next

    if cur is None:
        return 



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print(print_nth_from_last(llist, 4,1))
# print(llist.print_nth_from_last(4,2))