s=input()

# print(s[::-1])

rev=""

# for i in s:
#     rev=i+rev
# print(rev)

i = len(s)-1
while(i>=0):
    rev=rev+s[i]
    i=i-1
print(rev)



