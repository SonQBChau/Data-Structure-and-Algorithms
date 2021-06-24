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
    elif method == 3:
        return 
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