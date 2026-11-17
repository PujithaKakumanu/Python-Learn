# In python charecters are acessed by using indexing  and slicing. 
# Indexing starts from zero and negative indexing is also possible in python. 
# Slicing is used to get sub string of sequences. 
# It has starting point and endling point(ending point an be excluded).

s = "Hello World!"

for i in range(len(s)):
    print(s[i])

print(s[1:5])
print(s[0:])
print(s[:6])
print(s[-1:-6])


# charecter accessing using for loop and indexing.

s1 = "Kakumanu Pujitha"
for char in s1:
    print(char)

s2 = "Hello World!"
for i in range(len(s2)):
    print(s2[i])
