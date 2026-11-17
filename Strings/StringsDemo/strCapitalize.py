# capitalize method is used to convert the first character of a string to uppercase and the rest to lowercase.
# General syntax: string.capitalize()

s = "hello, welcome to the India. India is a beautiful country."
print(s.capitalize())

s = s.split()
print(s)
for i in range(len(s)):
    s[i] = s[i].capitalize()
print(" ".join(s))