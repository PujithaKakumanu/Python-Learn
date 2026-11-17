# In python strings are arrays of bytes representing unicode characters. 
# However, python does not have a character data type
# a single character is simply a string with a length of 1.

# Strings can be accessed using indexing and slicing.
# Slicing is used to get a substring of sequences.
# It has a starting point and an ending point (the ending point can be excluded).
# It also has staring, ending point and step value. The step value is used to skip the characters in the string.

# : → Start and stop.
# :: → Start, stop and step.
# [::-1] → Reverse the string.

s = "Hello World!"

print(s[:]) # prints the entire string
print(s[0:5]) # indexing starts from 0 and ends at 4
print(s[6:11]) # indexing starts from 6 and ends at 10
print(s[0:11:2]) # indexing starts from 0 and ends at 10, with a step of 2

print(s[-1:-7:-1]) #negative indexing starts from -1 and ends at -7, with a step of -1
print(s[-7:-1]) #negative indexing starts from -7 and ends at -1
print(s[::-1]) #reversing the string