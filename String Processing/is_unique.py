# Python dictionary to solve the problem in linear time complexity, 
# but because of the additional data structure, the space complexity is also linear.
def is_unique(input_str):
    d = dict()
    input = ''.join(input_str.lower())
    
    for i in input:
        if i not in d:
            d[i] = 1
        else:
            return False
    
    return True

def is_unique_2(input_str):
    return len(set(input_str)) == len(input_str)

def is_unique_3(input_str):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
    for i in input_str:
        if i in alpha:
            alpha = alpha.replace(i, "")
        else:
            return False
    return True

print(is_unique('abCDefGh'))
print(is_unique('nonunique'))