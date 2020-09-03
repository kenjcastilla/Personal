name = 'ada lovelace'
print(name.upper())
print(name.lower())

first_name = 'ada'
last_name = 'lovelace'
full_name = f"{first_name} {last_name}"
print(full_name)

print(f'Hello, {full_name.title()}!')

# the .rstrip() method eliminates whitespace to the right of a string
# the .lstrip() method eliminates whitespace to the left of a string
# the .strip() method eliminates whitespace to the left and right of a string

# 3 * 3 = 9
# 3 ** 3 = 27

print(4/2)
print(14_000_000_000)

x, y, z = 0, 15, 6
print(y)
print(x)
print(z)

# There are no built-in constant types in Python, but you can still show if you want a variable treated as such by using all caps.
MAX_CONNECTIONS = 5000
