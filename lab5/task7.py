strings_list = ['aca', 'xyz', 'aba', '1221']
print("Sample List:", strings_list)

count = 0
for s in strings_list:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print("Expected Result :", count)
