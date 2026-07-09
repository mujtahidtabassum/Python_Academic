def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

def binary_search(sorted_lst, target):
    low = 0
    high = len(sorted_lst) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if sorted_lst[mid] == target:
            return mid
        elif sorted_lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

values = [10, 20, 30, 40, 50]
target = 30
print("List of values:", values)
print("Target to search:", target)
idx_linear = linear_search(values, target)
print(f"Linear Search: Target found at index {idx_linear}")
sorted_values = sorted(values)
idx_binary = binary_search(sorted_values, target)
print(f"Binary Search: Target found at index {idx_binary}")
