def find_naive(A):
    lowest_idx = 0
    for i in range(len(A)):
        if A[i] < A[lowest_idx]:
            lowest_idx = i
    return lowest_idx
  


x = find_naive([4, 5, 6, 7, 1, 2, 3]) #4
print(x)
x = find_naive([6, 7, 1, 2, 3, 4, 5])  # 2
print(x)
x = find_naive([7, 1, 2, 3, 4, 5, 6])  # 1
print(x)
x = find_naive([1, 2, 3, 4, 5, 6, 7])  # 0
print(x)
x = find_naive([3, 4, 5, 6, 7, 1, 2])  # 5
print(x)
x = find_naive([2, 3, 4, 5, 6, 7, 1])  # 6
print(x)
x = find_naive([5, 6, 7, 1, 2, 3, 5])  # 3
print(x)
