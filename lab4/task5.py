def count_distinct_elements(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    
    output_str = ", ".join([f"{key} => {val}" for key, val in counts.items()])
    print(output_str)

sample_list = [10, 20, 30, 30, 30, 30, 20, 40]
print("Sample List:", sample_list)
print("Sample output:")
count_distinct_elements(sample_list)
