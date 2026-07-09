starts_with = lambda string, sub: string.startswith(sub)

test_string = "Hello, world!"
sub_1 = "Hello"
sub_2 = "world"

print(f"String: '{test_string}'")
print(f"Checking prefix '{sub_1}':", starts_with(test_string, sub_1))
print(f"Checking prefix '{sub_2}':", starts_with(test_string, sub_2))
