from circular_linked_list import CircularLinkedList
def split_list(cllist):
    size = len(cllist)

    if size == 0:
        return None
    if size == 1:
        return cllist.head

    mid = size // 2
    count = 0
    prev = None
    cur = cllist.head

    while cur and count < mid:
        prev = cur
        cur = cur.next
        count += 1
    prev.next = cllist.head # first cllist

    split_cllist = CircularLinkedList()
    while cur.next != cllist.head:
        split_cllist.append(cur.data)
        cur = cur.next
    split_cllist.append(cur.data) 
    
    cllist.print_list()
    print("\n")
    split_cllist.print_list() 

# A -> B -> C -> D -> ...
# A -> B -> ... and C -> D -> ...

cllist = CircularLinkedList()
cllist.append("A")
cllist.append("B")
cllist.append("C")
cllist.append("D")
cllist.append("E")
cllist.append("F")

split_list(cllist)