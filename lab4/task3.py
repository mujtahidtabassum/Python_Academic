def is_palindrome(s):
    cleaned_s = "".join(s.split()).lower()
    return cleaned_s == cleaned_s[::-1]

user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
