def integer_square_root_naive(k):
    num = 1
    pow_num = num*num
    while pow_num <= k:
        num += 1
        pow_num = num*num

    return num - 1 


def integer_square_root(k):
    return 0


x = integer_square_root_naive(300)  # 17
y = integer_square_root(300)
print(x)
x = integer_square_root_naive(12)  # 3
y = integer_square_root(12)
print(x)
x = integer_square_root_naive(1000)  # 31
y = integer_square_root(1000)
print(x)
x = integer_square_root_naive(625)  # 25
y = integer_square_root(625)
print(x)
