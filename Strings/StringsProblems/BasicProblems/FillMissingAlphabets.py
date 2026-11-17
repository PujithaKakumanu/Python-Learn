# Remember:
# for loop → Checks each original character.
# while loop → Finds missing alphabets.
# ord() → Character to number.
# chr() → Number to character.

s=input()
res=""
for i in range(len(s)):
    res=res+s[i]
    if i<len(s)-1:
        j=ord(s[i])+1
        while j < ord(s[i+1]):
            res=res+ chr(j)
            j=j+1
print(res)
