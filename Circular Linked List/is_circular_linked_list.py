from circular_linked_list import CircularLinkedList

def is_circular_linked_list(input_list):
    if input_list.head:
        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
            return False
    else:
        return False

