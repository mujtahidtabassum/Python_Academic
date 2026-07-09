def reverse_words(s):
    words = s.split(" ")
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

sample_str = 'hello .py'
print("Sample string:", repr(sample_str))

result = reverse_words(sample_str)
print("Expected Result:", repr(result))
