from stack import Stack

def convert_int_to_bin(dec_num : int) -> str:
    if dec_num == 0:
        return 0
        
    curr_num = dec_num
    s = Stack()
    binary = ''
    while curr_num > 0:
        remainder = curr_num % 2
        curr_num = curr_num // 2 
        s.push(remainder)
    
    while not s.is_empty():
        binary += str(s.pop())
    
    return binary

print(convert_int_to_bin(242))