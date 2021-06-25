from singly_linked_list import LinkedList
def is_palindrome(llist,method) -> bool:
    # Solution 1: Using a string
    if method == 1:
        str = ''
        cur = llist.head
        while cur:
            str += cur.data
            cur = cur.next
        return str == str[::-1]
    # Solution 2: Using a stack
    elif method == 2:
        cur = llist.head
        stck = []
        while cur:
            stck.append(cur.data)
            cur = cur.next
        cur = llist.head
        while cur:
            data = stck.pop()
            if data != cur.data:
                return False
            cur = cur.next
        return True
    # Solution 3: Using Two Pointers 
    elif method == 3:
        if llist.head:
            p = llist.head
            q = llist.head
            prev = []

            i = 0
            # move q to the end of the linked list
            while q:
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i-1]

            count = 1
            
            while count <= i//2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True

         
    return False

# Example palindromes:
# RACECAR, RADAR

# Example non-palindromes:
# TEST, ABC, HELLO

llist = LinkedList()


llist_2 = LinkedList()
llist_2.append("A")
llist_2.append("B")
llist_2.append("C")

print(is_palindrome(llist,1))
print(is_palindrome(llist,2))
print(is_palindrome(llist,3))
print(is_palindrome(llist_2,1))
print(is_palindrome(llist_2,2))
print(is_palindrome(llist_2,3))