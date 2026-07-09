def find_max_min(lst):
    if not lst:
        return None, None
    
    max_val = lst[0]
    min_val = lst[0]
    
    for num in lst:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
            
    return max_val, min_val

numbers = [15, 3, 22, 91, 4, 78, -5, 0, 42]
print("List of numbers:", numbers)

maximum, minimum = find_max_min(numbers)
print("Maximum Value:", maximum)
print("Minimum Value:", minimum)
