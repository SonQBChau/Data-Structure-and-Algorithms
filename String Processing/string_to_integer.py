def str_to_int(input_str):

    output_int = 0

    if input_str[0] == '-':
        start_idx = 1
        is_negative = True
    else:
        start_idx = 0
        is_negative = False

    for i in range(start_idx, len(input_str)):
        place = 10**(len(input_str) - (i+1))
        digit = ord(input_str[i]) - ord('0')
        output_int += place * digit

    if is_negative:
        return -1 * output_int
    else:
        return output_int



s = "554"
x = str_to_int(s)
print(type(x))

s = "123"
print(str_to_int(s))

s = "-123"
print(str_to_int(s))

# input_str = 123
# len(input_str) = 3

# i = 0 
# place = 10** (3 - (0+1)) = 10** (2) = 100 
# i = 1
# place = 10** (3 - (1+1)) = 10** (1) = 10
# i = 2
# place = 10** (3 - (2+1)) = 10** (0) = 1