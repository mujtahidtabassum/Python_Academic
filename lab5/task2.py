def is_palindrome(s):
    cleaned_s = "".join(s.split()).lower()
    return cleaned_s == cleaned_s[::-1]

print("Check 'madam':", is_palindrome("madam"))
print("Check 'racecar':", is_palindrome("racecar"))
print("Check 'hello':", is_palindrome("hello"))

user_str = input("Enter a string: ")
if is_palindrome(user_str):
    print(f"'{user_str}' is a palindrome.")
else:
    print(f"'{user_str}' is not a palindrome.")
