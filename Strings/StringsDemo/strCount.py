# count method is used to count the number of occurrences of a substring in a string.
# General syntax: string.count(substring, start, end)
# The start and end parameters are optional and specify the range of the string to search.

s = "Kakumanu Pujitha, I am a 2026 Graduate, I love to learn Python and Machine Learning."
print(s.count("a")) # Count the occurrences of "a"
print(s.count("I",  0, 20)) # Count the occurrences of "I" in the first 20 characters

s1 = "pppppppuuuuuuujjjjjjjjaaaaaa"
print(s1.count("p")) # Count the occurrences of "p"
print(s1.count("p",0,4)) # Count the occurrences of "p" in the first 4 characters
