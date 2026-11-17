# strings provide a method called lower() which is used to convert all the characters in the string to lowercase.
# General syntax of string methods is: string.methodname()
# updatedtext = originaltext.methodname()

s = "Hello my name is PUJITHA KAKUMANU"
s1 = ""
print(s.lower())
print(s[0:15]+s[15:21].lower()+s[21:]) # converting only the characters from index 15 to 20 to lowercase

for i in range(len(s)):
    s1 +=s[i].lower()
    print(s[i].lower()) # converting each character to lowercase

print(s1)
