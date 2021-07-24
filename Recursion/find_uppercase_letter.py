def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    
    return "No uppercase character found"


def find_uppercase_recursive(input_str, idx=0):
    if idx >= len(input_str):
        return "No uppercase character found"
    if input_str[idx].isupper():
        return input_str[idx]
    else:
        idx += 1
        return find_uppercase_recursive(input_str, idx)

str_1 = "lucidProgramming"
str_2 = "LucidProgramming"
str_3 = "lucidprogramming"
x = find_uppercase_iterative(str_1)
print(x)
x = find_uppercase_iterative(str_2)
print(x)
x = find_uppercase_iterative(str_3)
print(x)
x = find_uppercase_recursive(str_1)
print(x)
x = find_uppercase_recursive(str_2)
print(x)
x = find_uppercase_recursive(str_3)
print(x)
