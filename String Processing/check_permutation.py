# Approach 1: Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(1)
def is_perm_1(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    
    if len(str_1) != len(str_2):
        return False
    
    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))
    
    n = len(str_1)
    
    for i in range(n):
        if str_1[i] != str_2[i]:
            return False
    
    return True

