text = input()

digits = 0
lowercase_letters = 0
uppercase_letters = 0
other_symbols = 0

for i in text:
    if i.isdigit():
        digits += 1
    elif i.islower():
        lowercase_letters += 1
    elif i.isupper():
        uppercase_letters += 1
    else:
        other_symbols += 1

print("Digits count: " + str(digits))
print("Lowercase letters count: " + str(lowercase_letters))
print("Uppercase letters count: " + str(uppercase_letters))
print("Other symbols count: " + str(other_symbols))

