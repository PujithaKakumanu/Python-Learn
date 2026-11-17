# Strip method is useful for cleaning the text received through input() ---> genrally used as input().strip()
# In python Strip method is used to remove the leading and trailing whitespaces from the string.
# General syntax of string methods is: string.methodname()
# It removes the whitespaces from the beginning and end of the string. 
# It does not remove the whitespaces from the middle of the string.

# strip() → Removes unwanted characters from both the left and right (beginning and ending).
# lstrip() →  Removes unwanted characters from the left (beginning).
# rstrip() →  Removes unwanted characters from the right (ending).

s = "   Hello my name is Pujitha Kakumanu   "

print(s.strip()) # removing leading and trailing whitespaces from the string
print(len(s.strip()))   


print(s.lstrip()) # removing leading whitespaces from the string
print(len(s.lstrip()))

print(s.rstrip()) # removing trailing whitespaces from the string
print(len(s.rstrip()))

# Removing specific characters
# You can also pass characters as arguments.
s = "Hello my name is Pujitha Kakumanu  "

print(s.strip("H")) # removing leading and trailing 'H' from the string
print(len(s.strip("H")))

print(s.lstrip("H")) # removing leading 'H' from the string
print(len(s.lstrip("H")))

print(s.rstrip("u  ")) # removing trailing 'u' from the string
print(len(s.rstrip("u  ")))