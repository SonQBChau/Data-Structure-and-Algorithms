def find(A, target):
    for i in range(len(A)):
        if A[i] == target:
            return i
    return None


A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108
x = find(A, target)
print(x)
