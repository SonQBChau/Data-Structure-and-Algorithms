# Linear Search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

# Iterative Binary Search
def binary_search_iterative(data, target):
    pass

# Recursive Binary Search
def binary_search_recursive(data, target, low, high):
    pass


data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 37

print(binary_search_recursive(data, target, 0, len(data)-1))
print(binary_search_iterative(data, target))
print(linear_search(data, target))
