# find method is used to find the index of the first occurrence of a substring in a string.
# General syntax: string.find(substring, start, end)
# The start and end parameters are optional and specify the range of the string to search.

s = "Python is a programming language. Python is widely used in web development, data science, and artificial intelligence."
print(s.find("is")) # Find the index of the first occurrence of "is"
print(s.find("Python")) # Find the index of the first occurrence of "Python"
print(s.find("Java")) # Find the index of "Java" (not found, returns -1)
 
