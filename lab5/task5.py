lst = [10, 20, 30, 20, 50]
print("Sample List:", lst)

for i in range(len(lst)):
    if lst[i] == 20:
        lst[i] = 200

print("Expected Result:", lst)
