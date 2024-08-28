# String Operations
s = "String Operations"
print("Centered String:", s.center(50, '-'))

# String Slicing
s1 = 'Hello World Hello World Hello World 1234'
print('String Slicing:', s1[0:5])

# Formatting Strings
name = 'Shreya'
surname = 'Chavan'
age = 19
print("Hello, my name is %s %s and age is %d" % (name, surname, age))

# StartsWith
print("\nStartsWith:", s1.startswith('s', 0, 6))

# EndsWith
print("EndsWith:", s1.endswith('s', 0, 6))

# Find
print('Finding "hello":', s1.find('hello', 0, 34))

# isalnum
print('\nisalphanumeric:', s1.isalnum())

# isnumeric
print('isnumeric:', s1.isnumeric())

# isalpha
print('isalpha:', s1.isalpha())

# isdigit
print('isdigit:', s1.isdigit())

# islower
print('islower:', s1.islower())

# isupper
print('isupper:', s1.isupper())

# isspace
print('isspace:', s1.isspace())

# istitle
print('istitle:', s1.istitle())

# Join
j = name.join('*')
print('Join:', j)

# Capitalize
print('\nCapitalize:', s.capitalize())

# Count
print('Count of "l":', s.count('l'))

# Lower
print('Lowercase:', s.lower())

# Replace
new_s = s.replace('Operations', 'Manipulations')
print('Replace:', new_s)

# Upper
print('Uppercase:', s.upper())

# Title
print('Title:', s.title())

# isdecimal
print('isdecimal:', s1.isdecimal())

# expandtabs
tab_string = "Hello\tWorld"
print('Expand Tabs:', tab_string.expandtabs(4))

# swapcase
mixed_case = "HeLLo WoRLD"
print('Swap Case:', mixed_case.swapcase())

# strip
whitespace_string = "   Hello World   "
print('Strip:', whitespace_string.strip())

# rfind
print('RFind "World":', s1.rfind('World'))

# rindex
print('RIndex "World":', s1.rindex('World'))

# split
split_string = "apple,orange,banana"
print('Split:', split_string.split(','))

# lstrip
print('Left Strip:', whitespace_string.lstrip())

# rstrip
print('Right Strip:', whitespace_string.rstrip())

# zfill
number = "42"
print('ZFill:', number.zfill(5))
