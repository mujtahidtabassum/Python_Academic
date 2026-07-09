lst = [10, 20, 30, 20, 50]
print("Sample List:", lst)

unique_lst = []
for num in lst:
    if num not in unique_lst:
        unique_lst.append(num)

print("Expected Result:", unique_lst)
