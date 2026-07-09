def unique_elements(lst):
    distinct_lst = []
    for item in lst:
        if item not in distinct_lst:
            distinct_lst.append(item)
    return distinct_lst

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
print("Sample List:", sample_list)

result = unique_elements(sample_list)
print("Sample output:", result)
