# Replace method is used to replace occurrences of a substring with another substring in a string.
# General syntax: string.replace(old_substring, new_substring, count)
# The count parameter is optional and specifies the maximum number of replacements to be made.

s = "Hello Welcome to the India, India is a beautiful country."
s1 = s.replace("India","USA") # Replace all occurrences of "India" with "USA"
s2 = s.replace("India","USA",1) # Replace only the first occurrence of "India" with "USA"
print(s1) 
print(s2) 


str = "Pujitha Kakumanu"
string1 = str.replace("Pujitha","Poojitha")
string =str.replace("u","oo")
print(string)
print(string1)