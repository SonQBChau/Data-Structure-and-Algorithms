from circular_linked_list import CircularLinkedList
def josephus_circle(cllist, step):
    cur = cllist.head
    length = len(cllist)

    while length > 1:
        count = 1
        while count != step:
            cur = cur.next
            count += 1
        print("KILL:" + str(cur.data))
        cllist.remove_node(cur)
        cur = cur.next
        length -= 1

    

cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)


josephus_circle(cllist, 2)
cllist.print_list()
