def find_naive(A):
    lowest_idx = 0
    for i in range(len(A)):
        if A[i] < A[lowest_idx]:
            lowest_idx = i
    return lowest_idx


def find(A):
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low + high) // 2

        if A[mid] > A[high]:
            low = mid + 1
        elif A[mid] <= A[high]:
            high = mid

    return low


# x = find_naive([4, 5, 6, 7, 1, 2, 3]) #4
# print(x)
# x = find_naive([6, 7, 1, 2, 3, 4, 5])  # 2
# print(x)
# x = find_naive([7, 1, 2, 3, 4, 5, 6])  # 1
# print(x)
# x = find_naive([1, 2, 3, 4, 5, 6, 7])  # 0
# print(x)
# x = find_naive([3, 4, 5, 6, 7, 1, 2])  # 5
# print(x)
# x = find_naive([2, 3, 4, 5, 6, 7, 1])  # 6
# print(x)
# x = find_naive([5, 6, 7, 1, 2, 3, 5])  # 3
# print(x)

x = find([4, 5, 6, 7, 1, 2, 3])  # 4
print(x)
x = find([6, 7, 1, 2, 3, 4, 5])  # 2
print(x)
x = find([7, 1, 2, 3, 4, 5, 6])  # 1
print(x)
x = find([1, 2, 3, 4, 5, 6, 7])  # 0
print(x)
x = find([3, 4, 5, 6, 7, 1, 2])  # 5
print(x)
x = find([2, 3, 4, 5, 6, 7, 1])  # 6
print(x)
x = find([5, 6, 7, 1, 2, 3, 5])  # 3
print(x)
