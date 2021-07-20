A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]


def find_closest_num_naive(A, target):
    min = float('inf')
    val = A[0]
    for i in range(len(A)):
        dif = abs(A[i] - target)
        if min > dif:
            min = dif
            val = A[i] 
    return val


print(find_closest_num_naive(A1, 11))
print(find_closest_num_naive(A2, 4))
