# Join method is used to concatenate the elements of an iterable (like a list) into a single string.
# General syntax: 'separator'.join(iterable)
# only itarable objects can be joined using the join() method. The iterable can be a list, tuple, or any other sequence of strings.

# separator can be any any Thing like a space, comma, hyphen, etc. It is used to separate the elements of the iterable in the resulting string.

s = "Hello welcome to the India, My name is Pujitha Kakumanu"
s1 = s.split() # Split the string into a list of words
s2 = "*".join(s1) # Join the list elements with a '*' separator
print(s2) 

s = "Java Python SQL"
s = s.split()
s = "-".join(s)
print(s)

s = "Hats And rats."
s = s.strip('.')
words = s.split()
words.sort(key=len) # Sort the list of words by length
s2 = " ".join(words) # Join the sorted list elements with a space separator
print(s2.capitalize()+".")