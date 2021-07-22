def find_highest_number_naive(A):
    peak = A[0]
    peak_pos = 0
    for i in range(len(A)):
        if A[i] > peak:
            peak = A[i]
            peak_pos = i
    if peak_pos == 0 or peak_pos == len(A)-1:
        return None
    if A[peak_pos-1] > A[peak_pos] and A[peak_pos] < A[peak_pos+1]:
        return None

    return A[peak_pos]

    

def find_highest_number(A):
    pass

# Peak element is "5".
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_highest_number(A))
print(find_highest_number_naive(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_highest_number(A))
print(find_highest_number_naive(A))
A = [1, 2, 3, 4, 5]
print(find_highest_number(A))
print(find_highest_number_naive(A))
A = [5, 4, 3, 2, 1]
print(find_highest_number(A))
print(find_highest_number_naive(A))
